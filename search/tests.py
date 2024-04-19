from django.test import TestCase
from django.urls import reverse, resolve
from search.views import SearchResultsListView

# testing url
class TestUrls(TestCase):

    def test_search_url(self):
        url = reverse('search:searchResult')
        self.assertEqual(resolve(url).func.view_class, SearchResultsListView)
