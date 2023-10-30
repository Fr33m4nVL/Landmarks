# Generated by Django 4.1 on 2023-10-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Excursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cost', models.IntegerField(default=0)),
                ('number', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
