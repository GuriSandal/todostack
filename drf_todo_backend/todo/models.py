from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Todo(models.Model):
    LOW = 'L'
    HIGH = 'H'
    MEDIUM = 'M'

    PRIORITY = [
        (LOW, 'Low'),
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
    ]

    todo_name = models.CharField(max_length=250, null=False)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITY, default=LOW)
    created_date = models.DateTimeField(auto_now=True, blank=False)
    owner = models.ForeignKey(
        'auth.User', related_name='todos', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.todo_name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
