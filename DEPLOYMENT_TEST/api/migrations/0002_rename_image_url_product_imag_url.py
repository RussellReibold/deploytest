# Generated by Django 4.1.7 on 2023-04-10 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_url',
            new_name='imag_url',
        ),
    ]
