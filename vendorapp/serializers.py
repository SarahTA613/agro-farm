from .models import Vendor
from rest_framework import serializers
from restapi_app.models import User 


class VendorRegisterSerializer(serializers.Serializer):
    full_name=serializers.CharField(max_length=100)
    dob=serializers.DateField()
    email=serializers.EmailField()
    password=serializers.CharField(max_length=100)
    password2=serializers.CharField(max_length=100)
    phn_number=serializers.CharField(max_length=20)
    address=serializers.CharField(max_length=255)
    business_name=serializers.CharField(max_length=100)
    business_address=serializers.CharField(max_length=100)
    business_size=serializers.CharField(max_length=100)
    adv=serializers.FileField()
    business_doc=serializers.FileField()
    nid_front=serializers.ImageField()
    nid_back=serializers.ImageField()
    nationality=serializers.CharField()

    def validate(self, data):
        email=data["email"]
        password=data["password"]
        password2=data["password2"]

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email Address Already Exists")
        
        if password!=password2:
            raise serializers.ValidationError("Doesn't matched confirm password")
        
        full_name=data["full_name"]
        dob=data["dob"]
        phn_number=data["phn_number"]
        address=data["address"]
        business_name=data["business_name"]
        business_address=data["business_address"]
        business_size=data["business_size"]
        adv=data["adv"]
        business_doc=data["business_doc"]
        nid_front=data["nid_front"]
        nid_back=data["nid_back"]
        nationality=data["nationality"]
        

       
        user=User(
            email=email,
            full_name=full_name,
            dob=dob,
            phn_number=phn_number,
            address=address,
            user_type="2",
            
            )
            
        user.set_password(password)
        user.save()

        vendor=Vendor(
            author=user,
            business_name=business_name,
            business_address=business_address,
            business_size=business_size,
            adv=adv,
            business_doc=business_doc,
            nid_front=nid_front,
            nid_back=nid_back,
            nationality=nationality,
        )
        vendor.save()
        
        
        return data