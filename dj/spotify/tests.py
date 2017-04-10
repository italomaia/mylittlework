from django.test import TestCase
from django.shortcuts import reverse


class TestSpotifySearch(TestCase):
    def test_empty_request_has_type_options(self):
        url = reverse('search-spotify')
        resp = self.client.get(url)

        self.assertContains(resp, 'track')
        self.assertContains(resp, 'album')
        self.assertContains(resp, 'artist')
        self.assertContains(resp, 'playlist')

    def test_search_returns_result(self):
        url = reverse('search-spotify') + '?q=home&type=track'
        resp = self.client.get(url)

        context = resp.context
        self.assertTrue(len(context['result']), 0)
