# Generated by Django 4.2 on 2023-10-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serializer', '0016_article_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='option',
        ),
        migrations.AddField(
            model_name='article',
            name='option1',
            field=models.CharField(blank=True, max_length=511, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='option2',
            field=models.CharField(blank=True, max_length=511, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='option3',
            field=models.CharField(blank=True, max_length=511, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='option4',
            field=models.CharField(blank=True, max_length=511, null=True),
        ),
    ]
