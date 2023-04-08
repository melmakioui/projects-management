# Generated by Django 4.2 on 2023-04-07 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comment_tasks', to='project_management.task'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comment_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
