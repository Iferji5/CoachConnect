import pytest
from django.contrib.auth import get_user_model
User = get_user_model()

@pytest.mark.django_db
def test_default_role_is_athlete():
    u = User.objects.create_user(username="a", password="x", email="a@a.com")
    assert u.role == User.ATHLETE
