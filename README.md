<p align="center">
    <a href="https://github.com/nickatnight/fastapi-spam/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/fastapi-spam/actions/workflows/main.yaml/badge.svg">
    </a>
    <a href="https://codecov.io/gh/nickatnight/fastapi-spam">
        <img alt="Coverage" src="https://codecov.io/gh/nickatnight/fastapi-spam/branch/main/graph/badge.svg?token=FUZyqlCbbl"/>
    </a>
    <a href="https://pypi.org/project/fastapi-spam/">
        <img alt="PyPi Shield" src="https://img.shields.io/pypi/v/fastapi-spam">
    </a>
    <a href="https://docs.astral.sh/uv/">
        <img alt="uv version" src="https://img.shields.io/badge/uv-0.7.18+-purple">
    </a>
    <a href="https://www.python.org/downloads/">
        <img alt="Python Versions Shield" src="https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white">
    </a>
    <a href="https://github.com/nickatnight/fastapi-spam/blob/master/LICENSE">
        <img alt="License Shield" src="https://img.shields.io/github/license/nickatnight/fastapi-spam">
    </a>
</p>

# 🍔 fastapi-spam

FastAPI middleware to redirect spam requests to a random 10 hours of video. Ported from [django-spam](https://github.com/Tivix/django-spam) (I'm the creator), which was inspired by this [Nick Craver Tweet](https://twitter.com/nick_craver/status/720062942960623616) from 2018.

## Installation

```bash
pip install fastapi-spam
```

## Usage

Add the `TenHoursOfRedirect` middleware to your FastAPI app (or Starlette).

```python
from fastapi import FastAPI

from fastapi_spam.middleware import TenHoursOfRedirect


app = FastAPI()

...

app.add_middleware(TenHoursOfRedirect)
```

Now, any time an intruder tries to access an endpoint in `SPAM_ROUTES`, they will be redirected to a random 10 hours of video...take that bots!
