# Generated by Django 2.1.7 on 2019-02-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_rsimagesmain'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylistadcreation',
            name='features',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propertylistadcreation',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='propertylistadcreation',
            name='offers',
            field=models.TextField(blank=True, null=True),
        ),
    ]
