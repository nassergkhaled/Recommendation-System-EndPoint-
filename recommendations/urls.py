from django.urls import path
from .views import UserDetailView, RecommendedApartmentsView

urlpatterns = [
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('recommendations/<int:user_id>/', RecommendedApartmentsView.as_view(), name='recommended-apartments'),
]

