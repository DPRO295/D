# Generated by Django 4.1.6 on 2023-03-12 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CS295P_Project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postthread',
            name='email',
        ),
        migrations.AddField(
            model_name='postthread',
            name='tip_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postthread',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
