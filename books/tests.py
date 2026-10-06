import pytest
from rest_framework.test import APIClient

from books.models import Book


@pytest.mark.django_db
def test_get_books():
    client = APIClient()

    response = client.get('/api/books/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_post_book():
    client = APIClient()

    data = {
        'title': '1984',
        'author': 'George Orwell',
    }

    response = client.post('/api/books/', data, format='json')

    assert response.status_code == 201
    assert Book.objects.filter(
        title='1984',
        author='George Orwell'
    ).exists()