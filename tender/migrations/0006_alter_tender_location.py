# Generated by Django 5.0.3 on 2024-04-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0005_alter_tender_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='Location',
            field=models.CharField(max_length=200),
        ),
    ]