# Generated by Django 4.2.7 on 2023-12-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlacuacheApp', '0006_remove_post_url_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
    ]
