from flask_testing import TestCase
from flask import url_for
from main import app_factory
import unittest


class TestConfig:
    TESTING = True


class SpotifyTestCase(TestCase):

    def create_app(self):
        return app_factory(TestConfig)

    def test_search_reploy_format(self):
        url = url_for('spotify-search', term='home', search_type='album')
        resp = self.client.get(url)
        first_item = resp.json[0]

        for key in first_item.keys():
            self.assertIn(key, ('name', 'thumb', 'url'))


if __name__ == '__main__':
    unittest.main()
