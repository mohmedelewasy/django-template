# Generated by Django 3.0.7 on 2020-08-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_apply_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='cv',
            field=models.FileField(upload_to='cv'),
        ),
    ]
