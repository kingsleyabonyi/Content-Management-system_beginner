from django.contrib import admin
from . models import Post, Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title)')}

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)

