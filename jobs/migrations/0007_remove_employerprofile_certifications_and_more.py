# Generated by Django 4.2.7 on 2023-11-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_employerprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employerprofile',
            name='certifications',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='portfolio_url',
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='location',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
    ]
