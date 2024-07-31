from django.contrib import admin
from .models import Book, Author, Blocklist

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Blocklist)
