from django.conf import settings


def test_celery_results_are_stored_in_postgres():
    assert "django_celery_results" in settings.INSTALLED_APPS
    assert settings.CELERY_RESULT_BACKEND == "django-db"


def test_ctgov_api_base_url_has_default(settings):
    assert settings.CTGOV_API_BASE_URL
