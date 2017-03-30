import requests
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, validate
from urllib.parse import urlencode


app = Flask('mylittlejob')

SPOTIFY_API = dict(
    search='https://api.spotify.com/v1/search?'
)


class SpotifySearchSchema(Schema):
    """Schema validator and serializer for spotify search consults."""

    term = fields.String(
        load_to='q',
        load_only=True,
        required=True,
        validate=validate.Length(min=1))

    search_type = fields.String(
        load_to='type',
        load_only=True,
        required=True,
        validate=validate.OneOf(
            [
                'album',
                'artist',
                'playlist',
                'track'
            ]
        ))


spotify_search_schema = SpotifySearchSchema()


@app.route("/spotify/search")
def spotify_search():
    """Searchs the spotify API."""
    # load and validate data
    data, errors = spotify_search_schema.load(request.args)

    if errors:
        return jsonify({'message': errors}), 400

    querystr = urlencode({
        'q': data['term'],
        'type': data['search_type']
    })

    resp = requests.get(SPOTIFY_API['search'] + querystr)
    data = resp.json()
    return jsonify(extract_items(data))


def pick_thumb(images):
    """
    Picks the image with the *most adequate* size.
    Returns a default value if no thumb-like image is found.
    """
    for img in images:
        if img['height'] >= 60 \
                and img['height'] <= 70 \
                and img['height'] == img['width']:
            return img['url']
    return 'https://placehold.it/64x64'


def extract_thumb(item):
    """Extracts an thumbnail from the available images."""
    images = []

    if 'images' in item:
        images = item['images']
    elif 'album' in item and 'images' in item['album']:
        images = item['album']['images']
    return pick_thumb(images)


def extract_url(item):
    """Extracts the result item spotify url."""
    if 'external_urls' in item:
        return item['external_urls'].get('spotify', None)


def extract_items(data):
    """Extracts itens from multiple types results."""
    results = []

    for result in data.values():
        for item in result['items']:
            results.append({
                'name': item['name'],
                'thumb': extract_thumb(item),
                'url': extract_url(item)
            })

    return results
