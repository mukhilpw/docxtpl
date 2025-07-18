from django.contrib import admin
from learn_docxtpl.models import BookDetails
# Register your models here.
class BookDetailsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'summary')

admin.site.register(BookDetails, BookDetailsAdmin)



