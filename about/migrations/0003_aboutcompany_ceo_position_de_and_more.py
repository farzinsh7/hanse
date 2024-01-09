# Generated by Django 5.0.1 on 2024-01-09 11:54

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_aboutcompany_ceo_image_aboutcompany_ceo_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutcompany',
            name='ceo_position_de',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='ceo_position_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='description_de',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='description_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='keywords_de',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='keywords_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='quote_de',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='quote_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='seo_description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='seo_description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='title_de',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='aboutcompany',
            name='title_en',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
