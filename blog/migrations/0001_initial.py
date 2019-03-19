# Generated by Django 2.1.7 on 2019-03-19 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('publish', models.DateField(default=datetime.datetime(2019, 3, 19, 12, 17, 55, 205611, tzinfo=utc))),
                ('slug', models.SlugField(default=1, max_length=250, unique_for_date='publish')),
                ('status', models.SmallIntegerField(choices=[(-1, '删除'), (0, '草稿'), (1, '发表'), (2, '热门')], default=0, max_length=10)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
