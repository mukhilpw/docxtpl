from django.contrib import admin
from learn_docxtpl.models import BookDetails, BookImage
# Register your models here.
class BookDetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'summary', 'image', 'images1')

admin.site.register(BookDetails, BookDetailsAdmin)

class BookImageAdmin(admin.ModelAdmin):
    list_display = ('book', 'image2')
admin.site.register(BookImage, BookImageAdmin)



