# Generated by Django 5.0.1 on 2024-01-22 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='bussines_line',
            field=models.CharField(max_length=200, null=True),
        ),
    ]