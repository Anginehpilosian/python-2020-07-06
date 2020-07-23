import re

from django.db import models


# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        # username
        if len(post_data['username']) < 2:
            print("Username should be at least 2 characters")
            errors["first_name"] = "Username should be at least 2 characters"
        # email
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(post_data['email']):
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
        # set up errors
        # check if the email is in the db - post data 'email'
        # if we did not find a user
            # generate errors
            # return redirect to login page to view errors
        # if we found a user
            # check if their password is the same
            # if it is the same
                # add id to session
                # redirect them to the account page
            # else
                # redirect them to loging page to view errors


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
