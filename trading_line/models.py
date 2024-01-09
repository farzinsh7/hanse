from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class TradingManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Trading(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish')
    )
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, unique=True)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='trading')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    keywords = models.CharField(max_length=300, null=True)
    seo_description = models.TextField(null=True)


    def __str__(self):
        return self.title

    objects = TradingManager()