# Generated by Django 5.0.1 on 2024-01-08 07:13

import ckeditor_uploader.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('about', ckeditor_uploader.fields.RichTextUploadingField()),
                ('contact_title', models.CharField(max_length=350)),
                ('image_vmv', models.ImageField(upload_to='home')),
                ('vision', ckeditor_uploader.fields.RichTextUploadingField()),
                ('mission', ckeditor_uploader.fields.RichTextUploadingField()),
                ('values', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('home_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='features', to='home.homedata')),
            ],
        ),
        migrations.CreateModel(
            name='CustomersReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='home/customers')),
                ('description', models.TextField(null=True)),
                ('home_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to='home.homedata')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(upload_to='home/slider')),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('home_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sliders', to='home.homedata')),
            ],
        ),
    ]
