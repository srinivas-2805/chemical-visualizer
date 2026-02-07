from django.urls import path
from .views import (
    LoginAPIView,          
    UploadCSVAPIView,
    DatasetHistoryAPIView,
    DatasetPDFAPIView,
    LatestDatasetAPIView,
)

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('upload-csv/', UploadCSVAPIView.as_view()),
    path('history/', DatasetHistoryAPIView.as_view()),
    path('report/<int:dataset_id>/', DatasetPDFAPIView.as_view()),
    path('latest/', LatestDatasetAPIView.as_view()),
]
