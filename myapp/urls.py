from django.urls import path,include
from .views import (
    CreateUserView ,LoginView ,UserDetailView
)
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet, DepartmentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('accounts/', CreateUserView.as_view(), name='create_account'),
    path('accounts/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
