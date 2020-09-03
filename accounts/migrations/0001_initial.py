# Generated by Django 3.0.7 on 2020-08-27 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('Cairo', 'Cairo'), ('Alexandria', 'Alexandria'), ('Gizeh', 'Gizeh'), ('Shubra El-Kheima', 'Shubra El-Kheima'), ('Port Said', 'Port Said'), ('Suez', 'Suez'), ('Luxor', 'Luxor'), ('al-Mansura', 'al-Mansura'), ('El-Mahalla El-Kubra', 'El-Mahalla El-Kubra')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
