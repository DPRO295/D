# Generated by Django 4.1.6 on 2023-05-18 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS295P_Project', '0012_postthread_taken_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]