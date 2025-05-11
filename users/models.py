from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg', blank=True)
    bio = models.TextField(blank=True, verbose_name='О себе')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    location = models.CharField(max_length=100, blank=True, verbose_name='Местоположение')

    def __str__(self):
        return f"Профиль {self.user.username}"

# Создание профиля автоматически при создании пользователя
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
