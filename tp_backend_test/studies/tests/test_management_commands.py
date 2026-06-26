import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command

pytestmark = pytest.mark.django_db


def test_seed_test_user_creates_idempotent_admin_user():
    user_model = get_user_model()

    call_command("seed_test_user")
    call_command("seed_test_user")

    user = user_model.objects.get(email="admin@example.com")
    assert user_model.objects.filter(email="admin@example.com").count() == 1
    assert user.is_staff is True
    assert user.is_superuser is True
    assert user.check_password("password123")
