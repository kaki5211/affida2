# Generated by Django 4.2 on 2023-10-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serializer', '0015_article_explain_article_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='option',
            field=models.CharField(blank=True, max_length=4095, null=True),
        ),
    ]
