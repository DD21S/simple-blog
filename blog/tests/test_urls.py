from django.test import TestCase
from django.urls import resolve, reverse

from blog import views

class Blog(TestCase):
    """
    Check that the urls of the blog app work 
    correctly and that they are well structured.
    """

    def test_posts_url_resolves(self):
        url = reverse('blog:posts')
        self.assertEquals(resolve(url).func, views.posts_view)

    def test_post_url_resolves(self):
        url = reverse('blog:post', args=['1'])
        self.assertEquals(resolve(url).func, views.post_view)

    def test_search_url_resolves(self):
        url = reverse('blog:search')
        self.assertEquals(resolve(url).func, views.search_view)

    def test_category_url_resolves(self):
        url = reverse('blog:category', args=['1'])
        self.assertEquals(resolve(url).func, views.category_view)
