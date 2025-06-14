# Generated by Django 5.2.2 on 2025-06-09 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='owner',
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
