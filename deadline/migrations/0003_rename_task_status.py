# Generated by Django 4.0.10 on 2024-07-20 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deadline', '0002_project_is_finish'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Status',
        ),
    ]