from django.urls import path
from accounts.auth.views import (
    ObtainAuthToken,
    registration_view
)


app_name = 'accounts'

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('login/', ObtainAuthToken.as_view(), name='login'),
]