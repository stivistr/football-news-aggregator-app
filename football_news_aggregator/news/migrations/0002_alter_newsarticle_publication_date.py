# Generated by Django 4.2.2 on 2023-08-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
