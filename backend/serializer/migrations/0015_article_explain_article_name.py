# Generated by Django 4.2 on 2023-10-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serializer', '0014_alter_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='explain',
            field=models.CharField(blank=True, max_length=1023, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='name',
            field=models.CharField(blank=True, max_length=1023, null=True),
        ),
    ]
