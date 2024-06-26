from django.contrib import admin
from .models import User, Apartment, UserInteraction

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email','alt_id')  # Display user IDs along with username and email
    search_fields = ('username', 'email')

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'recommended_score','alt_id')
    search_fields = ('title',)
    list_filter = ('price', 'recommended_score')

@admin.register(UserInteraction)
class UserInteractionAdmin(admin.ModelAdmin):
    list_display = ('user', 'apartment', 'rating','alt_id')
    search_fields = ('user__username', 'apartment__title')
    list_filter = ('rating',)

