# Generated by Django 4.1.3 on 2022-12-10 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]
