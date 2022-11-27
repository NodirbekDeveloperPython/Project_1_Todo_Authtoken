from django.contrib import admin
from django.urls import path
from plan.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('get_token/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
    path('plans/', AllPlansAPIView.as_view()),
    path('plan/<int:pk>/', PlanAPIView.as_view()),
    path('users/', UsersAPIView.as_view()),
]
