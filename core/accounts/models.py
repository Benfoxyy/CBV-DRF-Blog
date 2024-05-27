from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):

    def create_user(self,email,password,**extera_fields):
        if not email:
            raise ValueError(_("the email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extera_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extera_fields):
        extera_fields.setdefault("is_staff", True)
        extera_fields.setdefault("is_superuser", True)
        extera_fields.setdefault("is_verified", True)


        if extera_fields.get("is_staff") is not True:
            raise ValueError(_("is_staff must be True"))
        if extera_fields.get("is_superuser") is not True:
            raise ValueError(_("is_superuser must be True"))

        
        return self.create_user(email, password,**extera_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

class Profile (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    avatar = models.ImageField(blank=True,null=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.email
    
@receiver(post_save,sender=User)
def profile_saver(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)