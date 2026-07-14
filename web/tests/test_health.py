from django.urls import reverse
from django.test import RequestFactory

from web.views import health


def test_health_check():
    url = reverse("healthz")
    factory = RequestFactory()
    request = factory.get(url)

    response = health(request)

    assert response.status_code == 200
    assert response.data == {"status": "ok"}
