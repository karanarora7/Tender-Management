# Generated by Django 5.0.3 on 2024-04-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tender', '0009_alter_tender_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='Date',
            field=models.CharField(max_length=200),
        ),
    ]
