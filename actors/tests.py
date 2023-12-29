from django.test import TestCase, Client
import json
from .models import Actor


class ActorApiTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_actor_view(self):
        # Test GET request
        response = self.client.get('/actores/')  # Forneça a URL diretamente
        self.assertEqual(response.status_code, 200)

        # Test POST request
        data = {'name': 'TestActor'}
        response = self.client.post(
            '/actores/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        # Test duplicate POST request
        response = self.client.post(
            '/actores/', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_actor_detail_view(self):
        # Create a actor for testing
        actor = Actor.objects.create(name='TestActor')

        try:
            # Test GET request
            response = self.client.get(f'/actores/{actor.id}/')
            self.assertEqual(response.status_code, 200)

            # Test PUT request
            data = {'name': 'UpdatedActor'}
            response = self.client.put(
                f'/actores/{actor.id}/', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)

            # Test DELETE request
            response = self.client.delete(f'/actores/{actor.id}/')
            self.assertEqual(response.status_code, 204)

            # Test non-existing actor
            response = self.client.get('/actores/999/')
            self.assertEqual(response.status_code, 404)
        except Exception as e:
            print("Exception:", e)
            raise  # Reraise the exception to see the traceback
