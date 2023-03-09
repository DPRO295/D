# Generated by Django 4.1.6 on 2023-03-08 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CS295P_Project', '0020_delete_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postreward',
            old_name='dislikes',
            new_name='watches',
        ),
        migrations.RemoveField(
            model_name='postreward',
            name='likes',
        ),
        migrations.CreateModel(
            name='User_watched_Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CS295P_Project.postreward')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
