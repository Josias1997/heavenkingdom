from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255, help_text='Comma separated '
                                                               'keywords for research purpose')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class Track(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='music/files')
    meta_keywords = models.CharField(max_length=255, help_text='Comma separated '
                                                               'keywords for research purpose')
    categories = models.ManyToManyField('Category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
