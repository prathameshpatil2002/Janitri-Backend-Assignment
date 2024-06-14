from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Patient, HeartRateData
from .serializers import UserSerializer, PatientSerializer, HeartRateDataSerializer


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    try:
        user = User.objects.get(email=request.data['email'])
        if user.check_password(request.data['password']):
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', 'GET'])
def manage_patients(request):
    if request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_patient_details(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', 'GET'])
def heart_rate_data(request):
    if request.method == 'POST':
        serializer = HeartRateDataSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        data = HeartRateData.objects.all()
        serializer = HeartRateDataSerializer(data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_patient_heart_rate(request, patient_id):
    try:
        heart_rate_data = HeartRateData.objects.filter(patient_id=patient_id)
        if not heart_rate_data:
            return Response({"error": "No heart rate data found for this patient"}, status=status.HTTP_404_NOT_FOUND)
        serializer = HeartRateDataSerializer(heart_rate_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Patient.DoesNotExist:
        return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
