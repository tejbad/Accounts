from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# class UserProfile(models.Model):
    
class User(AbstractUser):
    # mob_no = models.BigIntegerField(default=00)
    clg_name = models.CharField(max_length=100 ,default="",blank=True)
    degree = models.CharField(max_length=100 ,default="",blank=True)
    passout_year = models.IntegerField(default=0,blank=True)
    course = models.CharField(max_length=100 ,default="",blank=True)
    school_name = models.CharField(max_length=100 ,default="",blank=True)
    age = models.IntegerField(default=0,blank=True)



class EmailBackend(object):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and  user.check_password(password):
                return user
        return None
    def get_user(self, user_id):
        User = get_user_model()        
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# class MobBackend(object):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         User = get_user_model()
#         try:
#             user = User.objects.get(mob_no=username)
#         except User.DoesNotExist:
#             return None
#         else:
#             if getattr(user, 'is_active', False) and  user.check_password(password):
#                 return user
#         return None
#     def get_user(self, user_id):
#         User = get_user_model()        
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None