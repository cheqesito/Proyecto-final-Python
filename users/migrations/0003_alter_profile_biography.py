# Generated by Django 4.0.2 on 2022-04-11 14:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_website_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
