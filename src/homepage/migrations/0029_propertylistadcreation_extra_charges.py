# Generated by Django 2.1.7 on 2019-03-18 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0028_propertylistrooms_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylistadcreation',
            name='extra_charges',
            field=models.CharField(default='2000', max_length=4),
        ),
    ]