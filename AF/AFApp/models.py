from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
  def create_user(self,email,name,phone_number,password=None):
    if not email:
      raise ValueError("Must enter email")
    user=self.model(
      email=self.normalize_email(email),
      name=name,
      phone_number=phone_number
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self,email,name,phone_number,password):
    user=self.create_user(email,name,phone_number,password)
    user.is_admin=True
    user.save(using=self._db)
    return user
class User(AbstractBaseUser):
  name=models.CharField(max_length=200)
  email=models.EmailField(unique=True)
  phone_number=models.CharField(max_length=15)
  is_active=models.BooleanField(default=True)
  is_admin=models.BooleanField(default=False)

  objects=UserManager()

  USERNAME_FIELD='email'
  REQUIRED_FIELDS=['name','phone_number']
  def __str__(self):
    return self.email
  def has_perm(self,perm,obj=None):
    return self.is_admin
  def has_module_perms(self,app_label):
    return self.is_admin
  
