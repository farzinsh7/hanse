from django.db import models

# Create your models here.
class SiteInformation(models.Model):
    title = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo', null=True)
    description = models.TextField(null=True)
    phone = models.CharField(max_length=11, null=True)
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