# Generated by Django 4.2.7 on 2023-11-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='phone_number',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employer',
            old_name='phone_number',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='custom_admin',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='password1',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='password2',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='last_name',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='password1',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='password2',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employer',
            name='username',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
