from django.utils import timezone
from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

class Author(models.Model):
    """ Information about the author of the posts.  """

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name + " " + self.lastname 

class Category(models.Model):
    """ Name of blog categories """
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    """ 
    Blog posts. With RichTextField input for 
    better appreciation of the information. 
    """

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    name = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    text_post = RichTextField()
    image_post = models.ImageField(upload_to="posts_images/")
    datetime = models.DateTimeField(default=timezone.now)
    readings = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, blank=True)

    def readings_counter(self):
        self.readings += 1
        self.save()
        return self.readings

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    """ Comments for each blog post """

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    text_comment = models.TextField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    