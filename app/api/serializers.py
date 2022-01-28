from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ..models import *

__all__ = ['RegisterSerializer', 'UserSerializer', 'StatusGETSerializer', 'StatusPOSTSerializer']


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True,
                                     validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    
    password  = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model  = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'birth_date', 'profile_pic')
        extra_kwargs = {
            'username': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        return attrs

    def create(self, validated_data):
        
        obj = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birth_date=validated_data['birth_date']
        )
        
        obj.set_password(validated_data['password'])
        obj.save()

        return obj



class UserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields =['id','username','first_name','last_name','birth_date']



class StatusGETSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Status
        fields = ['id', 'status', 'created_by', 'created_date_time']
        
class StatusPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"