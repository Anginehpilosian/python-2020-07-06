from django.db import models

# Create your models here.


class StudentManager(models.Manager):
    def basic_validatorzzz(self, post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(post_data['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        return errors


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # shirts
    # clubs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = StudentManager()


class ShirtManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(post_data['brand']) < 2:
            errors["brand"] = "Brand should be at least 2 characters"
        if post_data['size'] not in ['xs', 's', 'm', 'l', 'xl']:
            errors["size"] = "Size should be at ['xs', 's', 'm', 'l', 'xl']"
        if len(post_data['color']) < 3:
            errors["color"] = "Color should be at least 2 characters"
        return errors


class Shirt(models.Model):
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=255)
    brand = models.CharField(max_length=45)
    owner = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="shirts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShirtManager()


class Club(models.Model):
    name = models.CharField(max_length=255)
    # more fields?
    students = models.ManyToManyField(Student, related_name="clubs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
