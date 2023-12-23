from django.urls import path

from accounts.views import RegisterView, VerifyEmail

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),

]
