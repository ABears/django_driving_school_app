# Generated by Django 2.2.1 on 2019-05-19 10:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20190519_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='sys_id',
            field=models.AutoField(default=uuid.UUID('b3b661e0-fb50-4952-a539-b307c25e52bd'), primary_key=True, serialize=False),
        ),
    ]