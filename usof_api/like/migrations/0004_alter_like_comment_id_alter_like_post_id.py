# Generated by Django 4.2.6 on 2023-11-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usof_api_like', '0003_rename_author_of_like_like_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='comment_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='post_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
