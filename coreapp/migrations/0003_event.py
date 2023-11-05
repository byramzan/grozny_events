# Generated by Django 3.2.5 on 2023-11-04 14:35

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0002_meeting_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.TextField(max_length=500)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='coreapp.meeting')),
            ],
        ),
    ]
