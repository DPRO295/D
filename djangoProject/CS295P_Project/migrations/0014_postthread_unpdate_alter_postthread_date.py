# Generated by Django 4.1 on 2023-02-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS295P_Project', '0013_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postthread',
            name='unpdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='postthread',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
