# Generated by Django 3.1.6 on 2021-06-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My blog ', max_length=255),
        ),
    ]
