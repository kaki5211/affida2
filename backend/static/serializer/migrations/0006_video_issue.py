# Generated by Django 4.2 on 2023-07-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serializer', '0005_label_name_eng_maker_name_eng_performer_name_eng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='issue',
            field=models.DateField(blank=True, null=True),
        ),
    ]