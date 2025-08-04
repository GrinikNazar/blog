from django.contrib import admin

from .models import Tag, Author, Post


class TagAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'publication_date', 'tag', )
    list_display = ('title', 'publication_date', 'author')


admin.site.register(Tag, TagAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
