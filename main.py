"""
    TODO: Replace
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def main(request: Request):
    """Return a ``Coroutine`` of the ``index.html`` template and the ``request`` value."""
    return templates.TemplateResponse("index.html", {"request": request})
