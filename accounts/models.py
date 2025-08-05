from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=10)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    image = models.ImageField(upload_to="profile/", blank=True, null=True)

    def __str__(self):
        return self.name
