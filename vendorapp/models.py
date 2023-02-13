from django.db import models
from restapi_app.models import User
from django_countries.fields import CountryField

# Create your models here.

class Vendor(models.Model):
    author=models.OneToOneField(User,related_name="author",on_delete=models.CASCADE)
    business_name=models.CharField(max_length=100)
    business_address=models.CharField(max_length=255) 
    business_size=models.PositiveBigIntegerField(default=5) 
    adv=models.FileField(upload_to="media/adv")
    business_doc=models.FileField(upload_to="media/documents",verbose_name="Business Documents")
    nid_front=models.ImageField(upload_to="media/nid_front")
    nid_back=models.ImageField(upload_to="media/nid_back")
    nationality=CountryField(default="BD")
    date_at=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.author)
    

