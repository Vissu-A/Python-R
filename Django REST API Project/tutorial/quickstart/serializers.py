from django.contrib.auth.models import User, Group
from quickstart.models import userdata
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
# from rest_framework_mongoengine.serializers import DocumentSerializer
# from quickstart.models import mongouserdata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password','is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email = validated_data["email"],
            username = validated_data["username"],
            is_staff = 1,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
        	


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class UserdataSerializer(serializers.ModelSerializer):
	class Meta:
		model = userdata
		fields = ('username','password','email')
		# fields = '__all__'
		