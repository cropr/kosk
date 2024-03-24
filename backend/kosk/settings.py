#    Copyright 2022 Chessdevil Consulting

import os, os.path
import logging
from pathlib import Path

# paths

COLORLOG = False

FILESTORE = {
    "manager": "google",
    "bucket": os.environ.get("FILESTORE_BUCKET", "kosk-website-321608.appspot.com"),
}

LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(levelname)s: %(asctime)s %(name)s %(message)s",
        },
        "color": {
            "format": "%(log_color)s%(levelname)s%(reset)s: %(asctime)s %(bold)s%(name)s%(reset)s %(message)s",
            "()": "reddevil.core.colorlogfactory.c_factory",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "kosk": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "reddevil": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "fastapi": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

KOSK_MODE = os.getenv("KOSK_MODE", "production")

SECRETS_PATH = Path(os.environ.get("SECRETS_PATH", ""))

TOKEN = {
    "timeout": 180,  # timeout in minutes
    "secret": "kennehvrowe,endaklaagtendazaagt",
    "algorithm": "HS256",
    "nocheck": False,
}

ls = "No local settings found"

if KOSK_MODE == "local":
    ls = "importing local settings"
    from env_local import *

if COLORLOG:
    LOG_CONFIG["handlers"]["console"]["formatter"] = "color"  # type: ignore

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)
logger.info(ls)
