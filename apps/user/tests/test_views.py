import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

client = APIClient()


@pytest.mark.django_db
def test_register_user_success():
    user_data = {
        'username': 'testuser',
        'password': 'S@qwryuiqwhejqjwlekjqwkle1312312',
        'password2': 'S@qwryuiqwhejqjwlekjqwkle1312312'
    }

    url = reverse('register')
    response = client.post(url, user_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username='testuser').exists()


@pytest.mark.django_db
def test_register_user_invalid_data():
    user_data = {
        'username': 'testuser',
        'password': 'S@qwryuiqwhejqjwlekjqwkle1312312'
    }
    url = reverse('register')
    response = client.post(url, user_data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
