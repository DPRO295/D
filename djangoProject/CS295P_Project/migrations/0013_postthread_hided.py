# Generated by Django 3.2.18 on 2023-05-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS295P_Project', '0012_postthread_taken_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='postthread',
            name='hided',
            field=models.IntegerField(default=0),
        ),
    ]
