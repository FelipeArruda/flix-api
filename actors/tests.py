from django.test import TestCase, Client
import json
from .models import Actor


class ActorApiTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_actor_view(self):
        # Test GET request
        response = self.client.get('/api/v1/actors/')  # Adjusted URL
        self.assertEqual(response.status_code, 200)

        # Test POST request
        data = {'name': 'TestActor'}
        response = self.client.post(
            '/api/v1/actors/', data=json.dumps(data), content_type='application/json')  # Adjusted URL
        self.assertEqual(response.status_code, 201)

        # Test duplicate POST request
        response = self.client.post(
            '/api/v1/actors/', data=json.dumps(data), content_type='application/json')  # Adjusted URL
        self.assertEqual(response.status_code, 400)

    def test_actor_detail_view(self):
        # Create an actor for testing
        actor = Actor.objects.create(name='TestActor')

        try:
            # Test GET request
            response = self.client.get(
                f'/api/v1/actors/{actor.id}/')  # Adjusted URL
            self.assertEqual(response.status_code, 200)

            # Test PUT request
            data = {'name': 'UpdatedActor'}
            response = self.client.put(
                f'/api/v1/actors/{actor.id}/', data=json.dumps(data), content_type='application/json')  # Adjusted URL
            self.assertEqual(response.status_code, 200)

            # Test DELETE request
            response = self.client.delete(
                f'/api/v1/actors/{actor.id}/')  # Adjusted URL
            self.assertEqual(response.status_code, 204)

            # Test non-existing actor
            response = self.client.get('/api/v1/actors/999/')  # Adjusted URL
            self.assertEqual(response.status_code, 404)
        except Exception as e:
            print("Exception:", e)
            raise  # Reraise the exception to see the traceback
