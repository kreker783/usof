# Generated by Django 4.2.6 on 2023-10-31 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usof_api_categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
