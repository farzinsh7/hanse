# Generated by Django 5.0.1 on 2024-01-10 06:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_brandimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='customersreview',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customersreview',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customersreview',
            name='position_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customersreview',
            name='position_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='features',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='features',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='features',
            name='title_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='features',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='helpfullinks',
            name='title_de',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='helpfullinks',
            name='title_en',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='about_de',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='about_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='mission_de',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='mission_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='title_de',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='title_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='values_de',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='values_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='vision_de',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='homedata',
            name='vision_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='address_de',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='address_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='title_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='title_en',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
