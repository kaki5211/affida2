# Generated by Django 4.2 on 2023-10-15 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serializer', '0011_article_video_affiliateurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='top_image',
            field=models.CharField(blank=True, max_length=1023, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='affiliateurl',
            field=models.CharField(blank=True, max_length=1023, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]