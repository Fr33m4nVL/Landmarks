# Generated by Django 4.1 on 2023-10-28 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landmarks', '0002_landmark_preview_alter_landmark_coordinate_1_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
