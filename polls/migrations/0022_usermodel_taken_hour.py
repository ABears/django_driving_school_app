# Generated by Django 2.2.1 on 2019-06-10 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20190609_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='taken_hour',
            field=models.IntegerField(default=0),
        ),
    ]
