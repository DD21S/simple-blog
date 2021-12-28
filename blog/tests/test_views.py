import os

from django.conf import settings
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse

from blog.models import Author, Post, Category

class PostsTestView(TestCase):
    """
    Check that the views of the products app work 
    correctly and that they are well structured.
    """

    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(
            name="John",
            lastname="Room",
            url="https://urlurlurl.url",
        )
        self.post = Post.objects.create(
            name="Hello, Hi, Hey",
            author=self.author,
            description="Bye, Goodbye",
            text_post="Hello, Hi, Hey... Bye, Goodbye",
            image_post=SimpleUploadedFile(
                name='test_image.jpg',
                content=open(os.path.join(
                    settings.BASE_DIR, 'blog/tests/test_image.jpg'),
                    'rb'
                ).read(),
                content_type='image/jpeg',
            ),
        )

    def test_posts_view(self):
        response = self.client.get(reverse('blog:posts'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/posts.html')
        self.assertContains(response, self.post.name)

    def test_post_view(self):
        response = self.client.get(reverse('blog:post', args=[self.post.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post.html')
        self.assertContains(response, self.post.name)

    def test_search_view(self):
        response = self.client.post(
            reverse('blog:search'),
            {'search': 'Hello'}
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/search.html')
        self.assertContains(response, self.post.name)

    def test_search_not_results_view(self):
        response = self.client.post(
            reverse('blog:search'),
            {'search': 'Lorem'}
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/search.html')
        self.assertContains(response, "No se han encontrado resultados")

    def test_category_view(self):
        cat = Category(name="Programming")
        cat.save()

        response = self.client.get(reverse('blog:category', args=[1]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/category.html')
        self.assertContains(response, "No se han encontrado resultados")
