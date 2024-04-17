# Generated by Django 5.0.3 on 2024-04-11 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital', models.CharField(max_length=200)),
                ('Product', models.CharField(max_length=200)),
                ('Tender_Won_By', models.CharField(max_length=200)),
                ('Winning_Price', models.IntegerField(max_length=20)),
                ('Date', models.DateTimeField()),
            ],
        ),
    ]