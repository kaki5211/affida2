# Generated by Django 4.2 on 2023-07-07 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('productnumber', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=255, null=True)),
                ('views', models.IntegerField(blank=True, null=True)),
                ('kyounuki_post_day', models.DateField(blank=True, null=True)),
                ('producturl', models.URLField(blank=True, null=True)),
                ('label', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serializer.label')),
                ('maker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serializer.maker')),
                ('performers', models.ManyToManyField(blank=True, limit_choices_to={'is_active': True}, null=True, to='serializer.performer')),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serializer.series')),
                ('tags', models.ManyToManyField(blank=True, limit_choices_to={'is_active': True}, null=True, to='serializer.tag')),
                ('thumbnails', models.ManyToManyField(blank=True, null=True, to='serializer.thumbnail')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teststr', models.CharField(blank=True, max_length=255, null=True)),
                ('maker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serializer.maker')),
            ],
        ),
        migrations.CreateModel(
            name='Kyounuki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_day', models.DateField()),
                ('article', models.TextField()),
                ('productnumbers', models.ManyToManyField(to='serializer.video')),
            ],
        ),
    ]
