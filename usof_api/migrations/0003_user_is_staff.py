# Generated by Django 4.2.6 on 2023-10-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usof_api', '0002_alter_post_author_alter_post_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
