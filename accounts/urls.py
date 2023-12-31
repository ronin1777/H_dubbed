from django.urls import path

from accounts.views import RegisterView, VerifyEmail, UserListview, LoginAPIView, LogoutAPIView, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('user_list/', UserListview.as_view(), name="user_list"),
    path('user_list/<int:pk>', UserDetailView.as_view(), name="user_detail"),

    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('logout/', LogoutAPIView.as_view(), name="user_logout"),

]
