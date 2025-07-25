import random

from fastapi import FastAPI
from fastapi.testclient import TestClient

from fastapi_spam.constants import SPAM_ROUTES, TEN_HOURS_OF_FUN
from fastapi_spam.middleware import TenHoursOfRedirect


app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}


app.add_middleware(TenHoursOfRedirect)


def test_middleware_redirects_to_random_video() -> None:
    with TestClient(app, base_url="http://localhost:8000") as client:
        response = client.get(f"/{random.choice(SPAM_ROUTES)}", follow_redirects=False)

    assert response.status_code == 302
    assert response.headers.get("location") in TEN_HOURS_OF_FUN


def test_middleware_does_not_redirect_normal_routes() -> None:
    with TestClient(app, base_url="http://localhost:8000") as client:
        response = client.get("/", follow_redirects=False)

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
