from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):

    """Thi is the Custome User Model That Consist of the Basic Detais of the User."""
    email = models.EmailField(unique=True)

    bio = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    dob = models.DateField(_("Date of birth"), auto_now=False, auto_now_add=False)
    join_date = models.DateTimeField(_("Joined_Date"), auto_now_add=True)

    def __str__(self) -> str:
        return self.username
    

class NoteModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title