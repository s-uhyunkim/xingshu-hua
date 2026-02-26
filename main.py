"""
    TODO: Replace
"""

from typing import List, Dict, Any

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field


class SignaturePad(BaseModel):
    array: List[Dict[str, Any]] = Field(default_factory=list)
    # "= []" or "= Field(default=[])" work, but `default_factory` is recommended for explicit, instance-unique defaults

app = FastAPI()
templates = Jinja2Templates(directory="templates")
SIGNATURE_PAD = None


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root(request: Request):
    """Return a ``Coroutine`` of the ``index.html`` template and the ``request`` value."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signature-pad-data")
async def get_data(signature_pad: SignaturePad):
    global SIGNATURE_PAD
    SIGNATURE_PAD = signature_pad
    return RedirectResponse(url="/output", status_code=302)

@app.get("/output")
async def read_output(request: Request):
    """Return a ``Coroutine`` of the ``output.html`` template and the ``request`` and ``signature_pad`` values."""
    return templates.TemplateResponse("output.html", {"request": request, "signature_pad": SIGNATURE_PAD})
