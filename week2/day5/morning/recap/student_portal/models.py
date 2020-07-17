from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # shirts
    # clubs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Shirt(models.Model):
    size = models.CharField(max_length=5)
    color = models.CharField(max_length=255)
    brand = models.CharField(max_length=45)
    owner = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="shirts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Club(models.Model):
    name = models.CharField(max_length=255)
    # more fields?
    students = models.ManyToManyField(Student, related_name="clubs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
