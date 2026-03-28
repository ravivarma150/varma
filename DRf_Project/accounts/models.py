from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student'
    )

    # email already exists in AbstractUser
    # username already exists and is unique
    # password is handled & hashed automatically
    # date_joined is already present (auto_now_add)

    class Meta:
        db_table = 'accounts_user'

    def __str__(self):
        return self.username
