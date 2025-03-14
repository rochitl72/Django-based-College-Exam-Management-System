from django.urls import path
from .views import register_user, login_user, user_profile, user_list
from .views import register_user, login_user

urlpatterns = [
    path('', user_list, name='user-list'),  # ✅ Default `/api/users/` endpoint
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('profile/', user_profile, name='profile'),
]

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns += [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from .views import LogoutView

urlpatterns += [
    path('logout/', LogoutView.as_view(), name='logout'),
]
