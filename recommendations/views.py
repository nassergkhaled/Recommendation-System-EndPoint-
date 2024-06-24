from rest_framework import generics, viewsets
from rest_framework.exceptions import NotFound
import numpy as np
from .models import User, Apartment, UserInteraction
from .serializers import UserSerializer, ApartmentSerializer, UserInteractionSerializer

def get_recommended_apartments(user):
    interactions = UserInteraction.objects.all()

    if not interactions.exists():
        return Apartment.objects.none()

    user_ids = list(User.objects.values_list('id', flat=True))
    apartment_ids = list(Apartment.objects.values_list('id', flat=True))
    ratings_matrix = np.zeros((len(user_ids), len(apartment_ids)))

    for interaction in interactions:
        user_index = user_ids.index(interaction.user.id)
        apartment_index = apartment_ids.index(interaction.apartment.id)
        ratings_matrix[user_index][apartment_index] = interaction.rating

    def cosine_similarity(vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        norm_a = np.linalg.norm(vec1)
        norm_b = np.linalg.norm(vec2)
        return dot_product / (norm_a * norm_b)

    user_index = user_ids.index(user.id)
    user_ratings = ratings_matrix[user_index]
    similarities = []

    for i, other_user_ratings in enumerate(ratings_matrix):
        if i != user_index:
            similarity = cosine_similarity(user_ratings, other_user_ratings)
            similarities.append((user_ids[i], similarity))

    similarities.sort(key=lambda x: x[1], reverse=True)

    recommended_apartments = []
    recommended_scores = []

    for similar_user_id, _ in similarities[:5]:
        similar_user_ratings = ratings_matrix[user_ids.index(similar_user_id)]
        for apartment_index, rating in enumerate(similar_user_ratings):
            if rating > 0 and user_ratings[apartment_index] == 0:
                apartment = Apartment.objects.get(id=apartment_ids[apartment_index])
                recommended_apartments.append(apartment)
                recommended_scores.append(rating)

    for apartment, score in zip(recommended_apartments, recommended_scores):
        apartment.recommended_score = (apartment.recommended_score + score) / 2.0
        apartment.save()

    return recommended_apartments

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecommendedApartmentsView(generics.ListAPIView):
    serializer_class = ApartmentSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise NotFound('User not found')

        return get_recommended_apartments(user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class UserInteractionViewSet(viewsets.ModelViewSet):
    queryset = UserInteraction.objects.all()
    serializer_class = UserInteractionSerializer

