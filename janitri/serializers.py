from rest_framework import serializers
from .models import User, Patient, HeartRateData


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'name', 'age']


class HeartRateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartRateData
        fields = ['id', 'patient', 'heart_rate', 'timestamp']
