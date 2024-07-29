from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile
from django.dispatch import receiver

from django.db.models.signals import m2m_changed
from .models import Student, Course
from django.contrib import messages

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.userprofile.save()


@receiver(m2m_changed, sender=Student.courses.through)
def course_enrollment_changed(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add':
        print("data adddedd ....")