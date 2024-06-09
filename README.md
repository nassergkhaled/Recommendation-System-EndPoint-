# Recommendation System Endpoints

This project implements endpoints for a recommendation system using Django and Django REST Framework. The system allows users to retrieve information about users and apartments, as well as obtain personalized recommendations for apartments based on user interactions.

## Functionality

### Recommendation System Functionality:

1. **User Interaction Data**:
   - The system collects data on user interactions with apartments. This data typically includes user ratings for apartments they have interacted with.

2. **Collaborative Filtering**:
   - The recommendation system employs collaborative filtering to generate personalized recommendations for users.
   - Collaborative filtering identifies similarities between users based on their past interactions with apartments. Users who have interacted similarly with apartments are considered to have similar tastes and preferences.

3. **Cosine Similarity**:
   - Cosine similarity is used to quantify the similarity between the preferences of different users.
   - It calculates the cosine of the angle between two vectors representing user preferences. A higher cosine similarity indicates greater similarity in preferences.

4. **Generating Recommendations**:
   - For a given user, the system identifies similar users based on their interaction patterns.
   - It then recommends apartments that similar users have interacted with positively but the current user has not yet interacted with.
   - Recommendations are sorted based on their relevance to the user, with higher-rated apartments from similar users being prioritized.

### API Endpoints:

1. **Retrieve User Details**:
   - `GET /api/user/<user_id>/`: Retrieves details of the user with the specified ID.

2. **Get Recommended Apartments for User**:
   - `GET /api/recommendations/<user_id>/`: Retrieves recommended apartments for the user with the specified ID.

### Code Functionality:

1. **Models**:
   - The `models.py` file defines the data models for users, apartments, and user interactions.
   - Each model represents a table in the database, storing relevant information such as user details, apartment attributes, and user-apartment interactions.

2. **Serializers**:
   - The `serializers.py` file provides serializers for converting model instances to JSON format and vice versa.
   - Serializers facilitate data exchange between the Django application and the client by ensuring proper formatting of data.

3. **Views**:
   - The `views.py` file implements API endpoints using Django REST Framework's generic views.
   - Views define the behavior of each API endpoint, including handling requests, processing data, and returning responses.

4. **URL Patterns**:
   - The `urls.py` file defines URL patterns for routing requests to appropriate views.
   - URL patterns map URLs to corresponding views, ensuring that incoming requests are directed to the correct endpoints.

5. **Admin Interface**:
   - The `admin.py` file configures the Django admin interface to manage users, apartments, and user interactions.
   - Admin customization allows administrators to add, edit, and delete data through a user-friendly interface.

## How to Use

1. Clone the repository: `git clone <repository_url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the Django development server: `python manage.py runserver`

The API endpoints will be accessible at `http://127.0.0.1:8000/api/`.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
