from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated   # ✅ REQUIRED
from .models import Dataset
from .serializers import DatasetSerializer
from .utils import analyze_csv
from django.http import FileResponse
from .pdf_utils import generate_pdf
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny



class UploadCSVAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        if 'file' not in request.FILES:
            return Response(
                {"error": "CSV file is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        file = request.FILES['file']

        try:
            summary, _ = analyze_csv(file)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        dataset = Dataset.objects.create(
            name=file.name,
            summary=summary
        )

        datasets = Dataset.objects.order_by('-uploaded_at')
        if datasets.count() > 5:
            for old in datasets[5:]:
                old.delete()

        serializer = DatasetSerializer(dataset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DatasetHistoryAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        datasets = Dataset.objects.order_by('-uploaded_at')
        serializer = DatasetSerializer(datasets, many=True)
        return Response(serializer.data)

class DatasetPDFAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, dataset_id):
        try:
            dataset = Dataset.objects.get(id=dataset_id)
        except Dataset.DoesNotExist:
            return Response(
                {"error": "Dataset not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        pdf_buffer = generate_pdf(dataset)
        return FileResponse(
            pdf_buffer,
            as_attachment=True,
            filename=f"{dataset.name}_report.pdf"
        )

class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        print("USERNAME:", repr(username))
        print("PASSWORD:", repr(password))

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "token": token.key,
            "username": user.username
        })
    
class LatestDatasetAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        dataset = Dataset.objects.order_by('-uploaded_at').first()
        if not dataset:
            return Response({}, status=204)
        serializer = DatasetSerializer(dataset)
        return Response(serializer.data)
