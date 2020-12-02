from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import SignUpView, LogInView

app_name = 'authentication'

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('log_in/', LogInView.as_view(), name='log_in'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
