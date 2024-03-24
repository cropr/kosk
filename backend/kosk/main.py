# copyright Ruben Decrop 2012 - 2024
# copyright Chessdevil Consulting 2015 - 2024

import os.path
import logging, logging.config

from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from reddevil.core import register_app, get_settings
from dotenv import load_dotenv
import mimetypes
from kosk import VERSION

# load and register app
load_dotenv()
app = FastAPI(
    title="KOSK backend",
    description="backend website kosk.be",
    version=VERSION,
)
register_app(app, "kosk.settings", "/api")
settings = get_settings()
logger = logging.getLogger(__name__)
logger.info(f"Starting website kosk ...")

# import api endpoints
from reddevil.filestore import api_filestore
app.include_router(api_filestore.router)
logger.info(f"Api layer loaded")

# add CORS middleware for dev only
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#    Simplify operation IDs so that generated API clients have simpler function
#    names.
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.name[4:]
