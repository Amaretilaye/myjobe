# Generated by Django 4.2.7 on 2023-11-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_employeeprofile_bio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeprofile',
            name='skills',
        ),
        migrations.AddField(
            model_name='employeeprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, to='jobs.categories'),
        ),
    ]
