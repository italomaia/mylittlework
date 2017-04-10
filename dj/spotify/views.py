from django.views.generic import TemplateView

from .forms import SearchForm


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


class SpotifySearch(TemplateView):
    form_class = SearchForm
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET or None)
        context = self.get_context_data()
        context.update(dict(form=form))
        total = 0

        if form.is_bound and form.is_valid():
            response = form.query_api()
            json_data = response.json()
            total += sum([result.get('total', 0) for result in json_data.values()])

            context.update(dict(result=extract_items(json_data)))
            context.update(dict(total=total))

        return self.render_to_response(context)
