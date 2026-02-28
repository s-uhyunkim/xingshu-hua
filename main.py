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
    array: List[Dict[str, Any]] = Field(default_factory=list) # never rename var! I don't know why other names don't work
    # "= []" or "= Field(default=[])" work, but `default_factory` is recommended for explicit, instance-unique defaults

app = FastAPI()
templates = Jinja2Templates(directory="templates")
g_signature_pad = None


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root(request: Request):
    """Return a ``Coroutine`` of the ``index.html`` template and the ``request`` value."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signature-pad-data")
async def get_data(signature_pad: SignaturePad):
    global g_signature_pad
    g_signature_pad = signature_pad
    collapse_signature_pad()
    return RedirectResponse(url="/output", status_code=302)

@app.get("/output")
async def read_output(request: Request):
    """Return a ``Coroutine`` of the ``output.html`` template and the ``request`` and ``signature_pad`` values."""
    return templates.TemplateResponse("output.html", {"request": request, "signature_pad": g_signature_pad})

def collapse_signature_pad():
    global g_signature_pad
    strokes = g_signature_pad.array

    if g_signature_pad is None or len(strokes) < 2:
        return

    for i in range(1, len(strokes)):
        strokes[0]["points"] += strokes[1]["points"]
        strokes.pop(1)
