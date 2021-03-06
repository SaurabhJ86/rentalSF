# Generated by Django 2.1.7 on 2019-02-15 02:24

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20190213_0624'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=homepage.models.upload_image)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
