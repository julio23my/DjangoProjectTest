from django.contrib import admin
from .models import Book, BookNumber,Character, Author
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(BookNumber)
class BookNumberAdmin(admin.ModelAdmin):
    pass

admin.site.register(Character)
admin.site.register(Author)