# Generated by Django 3.0.7 on 2020-09-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_auto_20200907_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.CharField(auto_created=True, max_length=100, primary_key=True, serialize=False),
        ),
    ]