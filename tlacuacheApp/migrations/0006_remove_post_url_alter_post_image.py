# Generated by Django 4.2.7 on 2023-12-08 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlacuacheApp', '0005_alter_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
