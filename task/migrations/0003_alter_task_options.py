# Generated by Django 5.1.6 on 2025-03-01 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['done', '-created_at']},
        ),
    ]
