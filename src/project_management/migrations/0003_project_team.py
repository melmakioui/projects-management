# Generated by Django 4.2 on 2023-04-07 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0002_comment_task_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='team',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='team_project', to='project_management.team'),
            preserve_default=False,
        ),
    ]