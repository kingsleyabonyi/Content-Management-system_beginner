from django.db import models
import uuid
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    category_id =models.BigIntegerField(primary_key=True)
    slug = models.SlugField()



    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='img',)
    body = RichTextField()
    post_id = models.BigIntegerField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    # slug =models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
    


