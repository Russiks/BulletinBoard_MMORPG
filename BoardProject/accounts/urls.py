from django.urls import (
    path, include,
)
from django.contrib.auth.views import (
    LoginView, LogoutView,
)

from .views import (
    UserProfile, UpdateProfile, auth_code,
)

urlpatterns = [
    path('login/', LoginView.as_view(template_name='allauth/account/login.html'), name='account_login'),
    path('logout/', LogoutView.as_view(template_name='allauth/account/logout.html'), name='account_logout'),
    path('profile', UserProfile.as_view(), name='account_profile'),
    path('edit', UpdateProfile.as_view(), name='account_edit'),
    path('auth_code', auth_code, name='auth_code'),
    path('', include('allauth.urls')),
]