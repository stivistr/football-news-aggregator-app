# Generated by Django 4.2.2 on 2023-07-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
