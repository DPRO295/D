# Generated by Django 4.1.6 on 2023-03-08 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS295P_Project', '0018_comment_replies_userprofile_postreward_coinslog_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
