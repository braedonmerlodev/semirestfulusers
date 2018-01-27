from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
import bcrypt
from datetime import date
NAME_REGEX = re.compile(r'^[A-Za-z ]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData["full_name"]) < 1:
            errors.append("First name cannot be blank")
        elif len(postData["full_name"]) < 2:
            errors.append("First name must be at least 2 letters!")
        if len(postData["email"]) < 1:
            errors.append("Email must cannot be blank")
        elif not EMAIL_REGEX.match(postData["email"]):
            errors.append("Email address not valid")
        return errors


class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {}>".format(self.fullname, self.email)