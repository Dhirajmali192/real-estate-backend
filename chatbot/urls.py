from django.urls import path
from .views import analyze_area, download_data

urlpatterns = [
    path('analyze/', analyze_area),
    path('download/', download_data),  # <-- NEW
]

