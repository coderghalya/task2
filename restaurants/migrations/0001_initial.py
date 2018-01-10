# Generated by Django 2.0.1 on 2018-01-10 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('discription', models.TextField(blank=True, null=True)),
                ('opening_time', models.DateTimeField(auto_now=True)),
                ('closing_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
