from rest_framework.serializers import ModelSerializer
from .models import *
class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'password'