# Generated by Django 2.2.1 on 2019-06-01 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20190601_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointement',
            name='user_id',
        ),
        migrations.AddField(
            model_name='appointement',
            name='instructor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointement',
            name='student_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='instructor_class',
            name='instructor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_instructor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='instructor_class',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_student', to=settings.AUTH_USER_MODEL),
        ),
    ]
