from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from .models import UserInteraction, Apartment

@receiver(post_save, sender=UserInteraction)
def update_apartment_recommended_score(sender, instance, **kwargs):
    apartment = instance.apartment
    interactions = UserInteraction.objects.filter(apartment=apartment)
    if interactions.exists():
        avg_rating = interactions.aggregate(Avg('rating'))['rating__avg']
        apartment.recommended_score = avg_rating
        apartment.save()

