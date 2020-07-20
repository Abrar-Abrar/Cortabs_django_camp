# Generated by Django 3.0.7 on 2020-07-20 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.PositiveIntegerField()),
                ('create_at', models.DateField(default=datetime.date(2020, 7, 20))),
            ],
        ),
    ]
