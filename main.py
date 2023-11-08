from fastapi import FastAPI
from pydantic import BaseModel
from flow_data import flo_athletes, latest_new_headlines, upcoming_events

app = FastAPI(title="FLO-GRAPPLING", description="FLO GRAPPLING ", version="1.0.0")

# Model for address
class Headlines(BaseModel):
    headline: str

class Athletes(BaseModel):
    flo_athletes: str


class Events(BaseModel):
    get_events: str


@app.get("/athletes", response_model=dict, summary="All the current flo athletes")
async def get_athletes():
    athletes = flo_athletes()
    return athletes


@app.get("/headlines", response_model=dict, summary="latest flo headlines")
async def get_headlines():
    headlines = latest_new_headlines()
    return headlines


@app.get("/events", response_model=dict, summary="upcoming events")
async def get_events():
    events = upcoming_events()
    return events
