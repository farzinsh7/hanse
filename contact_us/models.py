from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name


class ContactUS(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="contact", null=True)
    address = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.title