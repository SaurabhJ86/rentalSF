# Generated by Django 2.1.7 on 2019-03-15 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0027_auto_20190315_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertylistrooms',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
