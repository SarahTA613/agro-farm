from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,full_name,dob,phn_number,address,profile=None,password=None,password2=None):
        if not email:
            raise ValueError('user must have email')
        user = self.model(
            email = self.normalize_email(email),
            full_name=full_name,
            dob=dob,
            phn_number=phn_number,
            address=address,
            profile=profile,
            

        )

        user.set_password(password)
        user.save(using = self._db)
        return user



    def create_superuser(self, email,full_name,dob,phn_number,address,profile=None,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            full_name=full_name,
            dob=dob,
            phn_number=phn_number,
            address=address,
            password=password,
            profile=profile,
            
        )
        user.is_admin = True
        user.user_type='1'
        user.is_superuser = True
        user.save(using=self._db)
        return user



    

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(
        verbose_name= 'email',
       
        unique= True,
    )
    full_name = models.CharField(max_length=200)
    user_type=models.CharField(max_length=1,choices=(("1","Administrator"),("2","Vendor"),("3","Customer")),default="3")
    dob = models.DateField()
    phn_number = models.CharField(max_length=20)
    address = models.TextField()
    profile = models.ImageField(upload_to="media/profile",default='media/profile/default.jpg')
   
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','dob','phn_number','address']

    def __str__(self):
        return self.email

    def has_perm(self,perm,object=None):
        "Does the user has a specific permission ?"
        return self.is_admin

    def has_module_perm(self, app_label):
        "Does the user have permission to view the app `app_label`"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin 
