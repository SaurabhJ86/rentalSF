# Generated by Django 2.1.7 on 2019-03-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0034_propertylistadcreation_bathrooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylistadcreation',
            name='lat',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='propertylistadcreation',
            name='lng',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
