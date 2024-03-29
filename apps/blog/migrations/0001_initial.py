# Generated by Django 3.2.3 on 2021-05-28 10:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('background_color', models.CharField(choices=[('yellow', 'yellow'), ('gray', 'gray'), ('red', 'red'), ('blue', 'blue'), ('teal', 'teal'), ('green', 'green'), ('purple', 'purple'), ('indigo', 'indigo')], default='yellow', max_length=10)),
                ('text_color', models.CharField(choices=[('black', 'black'), ('white', 'white')], default='black', max_length=10)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='TaggedWhatever',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_taggedwhatever_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_taggedwhatever_items', to='blog.customtag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('summary', models.TextField(max_length=250)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='posts/')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('published_at', models.DateTimeField(default=datetime.datetime.now)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='posts', through='blog.TaggedWhatever', to='blog.CustomTag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-published_at'],
            },
        ),
    ]
