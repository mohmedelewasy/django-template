# Generated by Django 3.0.7 on 2020-09-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0012_auto_20200907_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
