# Generated by Django 4.1.6 on 2023-05-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS295P_Project', '0015_remove_history_is_finished_postthread_reward_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
