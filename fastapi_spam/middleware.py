import random
import re
from typing import Optional

from starlette.responses import RedirectResponse
from starlette.types import ASGIApp, Receive, Scope, Send

from fastapi_spam.constants import SPAM_ROUTES, TEN_HOURS_OF_FUN


class TenHoursOfRedirect:
    def __init__(
        self,
        app: ASGIApp,
        additional_routes: Optional[list[str]] = None,
    ):
        self.app = app

        all_routes = SPAM_ROUTES + (additional_routes or [])
        escaped_routes = [re.escape(route) for route in all_routes]

        self.spam_pattern = re.compile(f"({'|'.join(escaped_routes)})$")

    async def __call__(self, scope: Scope, receive: Receive, send: Send):  # type: ignore
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        path = scope.get("path", "")

        if self.spam_pattern.search(path):
            response = RedirectResponse(
                url=random.choice(TEN_HOURS_OF_FUN), status_code=302
            )
            await response(scope, receive, send)
            return

        await self.app(scope, receive, send)
