# Generated by Django 4.0.10 on 2024-07-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deadline', '0003_project_ad_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='developer_image',
        ),
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
