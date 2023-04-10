import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

"""
Custom user model for django in case we want to later create a member area for payed servrices such as ChatGPT
As per documentation thish should be done early in the project

Link: https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model
"""

# Constants
EMAIL_VERBOSE = "Email address"


# TODO: Create a Password Validator that checks if the password is at least 10 Charas long
# Creates and saves user with mandatory fields
class UsrManager(BaseUserManager):
    def create_user(self, email, password, usrname=None):
        if not email:
            raise ValueError(f"{email} is not a valid Email address")

        usr = self.model(email=self.normalize_email(email), usrname=usrname)
        usr.set_password(password)
        usr.save(using=self._db)
        return usr

    #  Creates and saves a superuser with the given email, date of
    def create_superuser(self, email, password, usrname=None):
        user = self.create_user(
            email,
            password=password,
            usrname=usrname,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Core Django Usr class used for authentication
class Usr(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name=EMAIL_VERBOSE)
    usrname = models.CharField(unique=True, max_length=150, null=True)
    isActive = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UsrManager()

    # String represantation of Usr Object
    def __str__(self) -> str:
        return self.usrname if self.usrname else "Unknown"
    
    # Required methods for authentication backends
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    # Custom methods
    def is_superuser(self):
        return self.is_admin
    
    def is_staff(self):
        return self.is_staff

class Brand(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.id
       
# Product Table Model
class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    product_flavour = models.CharField(max_length=100, null=True)
    product = models.CharField(max_length=100, null=True)
    flavour = models.CharField(max_length=100, null=True)
    kilojoules = models.IntegerField(null=True)
    calories = models.IntegerField(null=True)
    fat = models.FloatField(null=True)
    saturated_fat = models.FloatField(null=True)
    carbohydrates = models.FloatField(null=True)
    sugar = models.FloatField(null=True)
    sodium = models.FloatField(null=True)
    dietary_fiber = models.FloatField(null=True)
    affiliate_link = models.CharField(max_length=200, null=True)
    brand_affiliate = models.CharField(max_length=200, null=True)
    source = models.CharField(max_length=100, null=True)
    on_amazon = models.CharField(max_length=100, null=True)
    amz_link = models.TextField(null=True)
    asin = models.CharField(max_length=100, null=True)
    protein = models.FloatField(null=True)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    energy = models.CharField(max_length=100, null=True)
    titel = models.CharField(max_length=100, null=True)
    imag_url = models.CharField(max_length=300, null=True)
    imag_url2 = models.CharField(max_length=300, null=True)

    

    def __str__(self):
        return self.id

# Blog Class
class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title