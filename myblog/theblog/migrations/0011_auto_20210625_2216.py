# Generated by Django 3.1.6 on 2021-06-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='bio',
            field=models.TextField(max_length=10),
        ),
    ]