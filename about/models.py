from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class AboutCompany(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="about")
    description = RichTextUploadingField()
    ceo_name = models.CharField(max_length=300, null=True)
    ceo_position = models.CharField(max_length=300, null=True)
    ceo_image = models.ImageField(upload_to="about", null=True)
    quote = RichTextUploadingField(null=True)
    keywords = models.CharField(max_length=300, null=True)
    seo_description = models.TextField(null=True)

    def __str__(self):
        return self.title