from django.test import TestCase, Client
import json
from .models import Genre


class GenreApiTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_genre_view(self):
        # Test GET request
        response = self.client.get('/api/v1/genres/')
        self.assertEqual(response.status_code, 200)

        # Test POST request
        data = {'name': 'TestGenre'}
        response = self.client.post(
            '/api/v1/genres/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # Test duplicate POST request
        response = self.client.post(
            '/api/v1/genres/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_genre_detail_view(self):
        # Create a genre for testing
        genre = Genre.objects.create(name='TestGenre')

        try:
            # Test GET request
            response = self.client.get(f'/api/v1/genres/{genre.id}/')
            self.assertEqual(response.status_code, 200)

            # Test PUT request
            data = {'name': 'UpdatedGenre'}
            response = self.client.put(
                f'/api/v1/genres/{genre.id}/', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)

            # Test DELETE request
            response = self.client.delete(f'/api/v1/genres/{genre.id}/')
            self.assertEqual(response.status_code, 204)

            # Test non-existing genre
            response = self.client.get('/api/v1/genres/999/')
            self.assertEqual(response.status_code, 404)
        except Exception as e:
            print("Exception:", e)
            raise  # Reraise the exception to see the traceback


