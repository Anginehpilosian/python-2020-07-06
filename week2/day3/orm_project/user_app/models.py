from django.db import models

# Create your models here.

class Shirt(models.Model):
    color = models.CharField(max_length=45)
    size = models.CharField(max_length=45)
    material = models.CharField(max_length=45)
    upload_by = models.ForeignKey("User", related_name="shirts", on_delete="cascade")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    social_security_number = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# User.objects.create(
# first_name="Leslie",
# last_name="D",
# email="leslie@dot.com",
# social_security_number="1234567890",
# password="i<3coding"
# )

# User.objects.all()

# from user_app.models import User
