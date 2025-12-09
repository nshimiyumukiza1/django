from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin'),
        ('user', 'User')
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        # Hash only if not already hashed
        if not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
