# Generated by Django 2.1.7 on 2019-03-31 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_datetime']},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['planned_date'], 'verbose_name_plural': 'Tasks'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='timestamp',
            new_name='comment_datetime',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='completed_on',
            new_name='accepted_date',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_accepted_on',
            new_name='completed_date',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='due_on',
            new_name='due_date',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='planned_on',
            new_name='planned_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_accepted_by',
        ),
        migrations.AddField(
            model_name='task',
            name='accepted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accepted_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(help_text='Press ctrl to select multiple', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='desc',
            field=models.TextField(blank=True, default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('PLAN', 'Planned'), ('PROG', 'In Progress'), ('COMP', 'Completed')], default='PLAN', max_length=4),
        ),
        migrations.AlterField(
            model_name='team',
            name='leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leading_teams', to=settings.AUTH_USER_MODEL),
        ),
    ]