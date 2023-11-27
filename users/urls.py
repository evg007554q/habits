from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.apps import UsersConfig
from users.views import UsersCreateAPIView

app_name = UsersConfig.name
# login/
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", UsersCreateAPIView.as_view(), name='register'),
    #
    # path('', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', UserUpdateView.as_view(), name='profile'),
    # path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    # path('check_email/<str:key>', check_email, name='check_email'),
    # # path('chm_send/<str:key>>', chm_send, name='chm_send'),
]





