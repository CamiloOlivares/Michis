from django.urls import path

from . import views
app_name = "animales_app"

urlpatterns = [
    path(
        'api/animales/list', views.AnimalListApiView.as_view(), name='animales'
    ),
    path(
        'api/animales/detail/<pk>', views.AnimalRetrieveAPIView.as_view(), name='animales'
    ),
    path('api/animales/create/', views.AnimalCreateAPIView.as_view()),
]
