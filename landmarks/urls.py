from django.urls import path

from .views import LandmarkList, LandmarkDetail

urlpatterns = [
    path('', LandmarkList.as_view(), name='landmarks'),
    path('landmark/<int:pk>/', LandmarkDetail.as_view(), name='landmark_detail'),
]