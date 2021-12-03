from django.urls import path, include
from . import views


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('logout/', views.LogoutAPIView.as_view(), name="logout")
]
