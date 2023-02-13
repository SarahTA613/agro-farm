from rest_framework import serializers
from restapi_app.models import User 


class CustomerRegisterSerializer(serializers.Serializer):
    full_name=serializers.CharField(max_length=100)
    dob=serializers.DateField()
    email=serializers.EmailField()
    password=serializers.CharField(max_length=100)
    password2=serializers.CharField(max_length=100)
    phn_number=serializers.CharField(max_length=20)
    address=serializers.CharField(max_length=255)
    
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
        
        

       
        user=User(
            email=email,
            full_name=full_name,
            dob=dob,
            phn_number=phn_number,
            address=address,
            
            
            )
            
        user.set_password(password)
        user.save()

        
        
        return data