# Generated by Django 2.1.7 on 2019-02-13 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontact',
            name='contact',
            field=models.CharField(max_length=14),
        ),
    ]
