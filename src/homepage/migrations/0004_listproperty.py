# Generated by Django 2.1.7 on 2019-02-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_rsimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownername', models.CharField(max_length=120)),
                ('property_type', models.CharField(max_length=120)),
                ('area', models.CharField(max_length=120)),
                ('contact', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
