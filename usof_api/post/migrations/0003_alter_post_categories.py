# Generated by Django 4.2.6 on 2023-11-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usof_api_categories', '0002_alter_category_description'),
        ('usof_api_post', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, to='usof_api_categories.category'),
        ),
    ]
