# Generated by Django 4.2.6 on 2023-10-31 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
