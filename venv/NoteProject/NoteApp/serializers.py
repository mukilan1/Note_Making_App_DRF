from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import NoteModel

# this is the User Model that is used to create the User Model. and this is piced from the settings file of the Django.
User = get_user_model()

# this is the Serializer for the User Model. It will be used to handel the user datas.
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','bio','dob','profile_image','join_date']
        extra_kwargs = {'join_date':{'read_only':True},'password':{'write_only':True}}

# this function is to validate and hash the password and the User data before storing it in the server.
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class NoteSerializer(ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ['id','title','description','user','created_at','updated_at']
        extra_kwargs = {'user':{'read_only':True}}

