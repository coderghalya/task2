# Generated by Django 2.0.1 on 2018-01-22 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='discription',
            new_name='description',
        ),
    ]
