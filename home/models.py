from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class HomeData(models.Model):
    title = models.CharField(max_length=250)
    about = RichTextUploadingField()
    image_vmv = models.ImageField(upload_to='home')
    vision = RichTextUploadingField()
    mission = RichTextUploadingField()
    values = RichTextUploadingField()

    def __str__(self):
        return self.title
    

class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='home/slider')
    link = models.CharField(max_length=200,blank=True,null=True)
    home_data = models.ForeignKey(HomeData, null=True, on_delete=models.SET_NULL, related_name='sliders')

    def __str__(self):
        return self.title
    

class Features(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100)
    description = models.TextField(null=True)
    home_data = models.ForeignKey(HomeData, null=True, on_delete=models.SET_NULL, related_name='features')

    def __str__(self):
        return self.title


class CustomersReview(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home/customers')
    description = models.TextField(null=True)
    home_data = models.ForeignKey(HomeData, null=True, on_delete=models.SET_NULL, related_name='customer')

    def __str__(self):
        return self.name


class BrandImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='home/brands')
    home_data = models.ForeignKey(HomeData, null=True, on_delete=models.SET_NULL, related_name='brands')

    def __str__(self):
        return self.title


class SiteInformation(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo', null=True)
    description = models.TextField(null=True)
    phone = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=300, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.title

    
class SocialLinks(models.Model):
    label = models.CharField(max_length=120, null=True)
    icon = models.CharField(null=True, max_length=200)
    link = models.CharField(max_length=200,blank=True,null=True)
    main_data = models.ForeignKey(SiteInformation, null=True, on_delete=models.SET_NULL, related_name='socials')

    def __str__(self):
        return self.label if self.label else "No Label"


class HelpfulLinks(models.Model):
    title = models.CharField(max_length=120, null=True)
    link = models.CharField(max_length=200,blank=True,null=True)
    main_data = models.ForeignKey(SiteInformation, null=True, on_delete=models.SET_NULL, related_name='links')

    def __str__(self):
        return self.title if self.title else "No Title"


class Subscriber(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email