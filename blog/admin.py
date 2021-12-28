from django.contrib import admin

from .models import Author, Category, Post, Comment

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    """
        Admin View for Author
    """
    list_display = ('name','lastname')
    list_filter = ('name',)
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    """
        Admin View for Category
    """
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    """
        Admin View for Post
    """
    list_display = ('name','author',)
    list_filter = ('datetime','categories',)
    readonly_fields = ('readings',)
    search_fields = ('name',)

class CommentAdmin(admin.ModelAdmin):
    """
        Admin View for Comment
    """ 
    list_display = ('post',)
    readonly_fields = ('text_comment',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
