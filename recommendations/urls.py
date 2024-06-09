from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ApartmentViewSet, UserInteractionViewSet, UserDetailView, RecommendedApartmentsView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'apartments', ApartmentViewSet)
router.register(r'user-interactions', UserInteractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('recommendations/<int:user_id>/', RecommendedApartmentsView.as_view(), name='recommended-apartments'),
]

