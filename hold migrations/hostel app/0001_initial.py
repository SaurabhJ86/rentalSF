# Generated by Django 2.1.7 on 2019-03-14 09:56

from django.db import migrations, models
import hostel.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to=hostel.models.farmViewImageUploadPath)),
                ('rooms', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cctv', models.BooleanField(default=True)),
                ('kitchen', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
            ],
        ),
    ]
