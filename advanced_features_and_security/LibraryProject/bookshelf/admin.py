from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') # show these columns
    list_filter = ('author', 'publication_year') # add filter on sidebar
    search_fields = ('title', 'author') # add search bar, enable search by title and author

# Register your models here.
admin.site.register(Book, BookAdmin)
