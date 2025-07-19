from django.db import models

# Create your models here.
class BookDetails(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    summary = models.TextField(blank=True)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    images1 = models.FileField(upload_to='book_images/', null=True, blank=True)

    
    def __str__(self):
        return f"{self.title} by {self.author}"

class BookImage(models.Model):
    book = models.ForeignKey(BookDetails, on_delete=models.CASCADE, related_name='images')
    image2 = models.ImageField(upload_to='book_images/',null=True, blank=True)

