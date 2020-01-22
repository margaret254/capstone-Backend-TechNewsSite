from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import New


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # extra_kwargs = {'password' : {'write_only':True,'required':True}}

    def create(self,validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id','title','desc','new_image','pub_date')
        