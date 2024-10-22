from django_use_email_as_username.models import BaseUser, BaseUserManager

# Create your models here.


class User(BaseUser):
    objects = BaseUserManager()