# Generated by Django 2.1.7 on 2019-02-15 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_listproperty'),
    ]

    operations = [
        migrations.AddField(
            model_name='listproperty',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
