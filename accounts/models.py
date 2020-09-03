from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    CITIES = (
        ('Cairo','Cairo'),
        ('Alexandria','Alexandria'),
        ('Gizeh','Gizeh'),
        ('Shubra El-Kheima','Shubra El-Kheima'),
        ('Port Said','Port Said'),
        ('Suez','Suez'),
        ('Luxor','Luxor'),
        ('al-Mansura','al-Mansura'),
        ('El-Mahalla El-Kubra','El-Mahalla El-Kubra'),
    )

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    country = models.CharField(max_length=100, choices = CITIES)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
