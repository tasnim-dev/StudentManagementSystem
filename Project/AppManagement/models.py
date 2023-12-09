from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUser(AbstractUser):

    USER = (
        (1, "admin"),
        (2, "Teacher"),
        (3, "Student"),
    )

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_img = models.ImageField(upload_to="Profile_Img")