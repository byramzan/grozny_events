# Generated by Django 3.2.5 on 2023-11-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
