import re

from django.db import models


# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        # username
        if len(post_data['username']) < 2:
            errors["first_name"] = "Username should be at least 2 characters"
        # email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern
            errors['email'] = "Invalid email address!"
        # password
        # min length
        if len(post_data['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        # match the password confirm
        if post_data['password'] != post_data['password_confirm']:
            errors["password_confirm"] = "Password does not match"
        return errors

    # def login_validator

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
