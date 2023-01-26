from rest_framework import serializers
from .models import User
from .models import Picture


# here it serialize the data passed to it through views
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# here it serialize the image passed from views page
class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['picture']
