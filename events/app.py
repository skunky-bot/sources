"""Minimal authenticated Skunky events ingestion service."""
import json

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import PlainTextResponse
from pydantic import ValidationError

from middleware import BodyLimitMiddleware, SignatureMiddleware
from models import EventPayload
from storage import append_ndjson, writable

app = FastAPI(title="Skunky Events", version="0.1.0")
app.add_middleware(SignatureMiddleware)
app.add_middleware(BodyLimitMiddleware)


@app.get("/healthz", response_class=PlainTextResponse)
def health():
    return "ok"


@app.post("/events")
async def receive_event(request: Request):
    try:
        payload = EventPayload.model_validate(json.loads(request.state.raw_body))
    except (json.JSONDecodeError, ValidationError, TypeError) as exc:
        raise HTTPException(status_code=400, detail="Invalid event payload") from exc
    if not writable():
        raise HTTPException(status_code=503, detail="Event store unavailable")
    line = payload.model_dump_json()
    append_ndjson(payload.event, line)
    return {"status": "ok"}
