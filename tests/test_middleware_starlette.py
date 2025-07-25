import random

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.testclient import TestClient

from fastapi_spam.constants import SPAM_ROUTES, TEN_HOURS_OF_FUN
from fastapi_spam.middleware import TenHoursOfRedirect


async def homepage(request: Request) -> JSONResponse:
    return JSONResponse({"message": "Hello, World!"})


routes = [Route("/", endpoint=homepage)]

app = Starlette(debug=True, routes=routes)


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
