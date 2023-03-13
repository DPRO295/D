# Generated by Django 4.1.6 on 2023-02-26 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CS295P_Project', '0015_remove_postthread_unpdate_alter_postthread_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='postthread',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postthread',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='User_liked_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CS295P_Project.postthread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]