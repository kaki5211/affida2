# Generated by Django 4.2 on 2023-10-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serializer', '0012_article_number_article_top_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
