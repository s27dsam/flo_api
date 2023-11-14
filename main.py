from fastapi import FastAPI
from flow_data import flo_athletes, latest_new_headlines, upcoming_events, filter_events_by_keyword
from models import Event_Names

app = FastAPI(title="FLO-GRAPPLING", description="FLO GRAPPLING ", version="1.0.0")

# lists all the athletes on the flo-grappling website
@app.get("/athletes", response_model=dict, summary="all the current flo athletes list on flo grappling")
async def get_athletes():
    athletes = flo_athletes()
    return athletes

# returns the upcoming events by type listed on the flo-grapplng website (ADCC,WNO,IBJJF)
@app.get("/events/{event_name}", summary='Find all the events by specific type (ADCC,WNO,IBJJF)')
async def get_event_type(event_name: Event_Names):
    if event_name is Event_Names.IBJJF:
        return {"event_name": event_name, "Events": filter_events_by_keyword(upcoming_events()['Upcoming Events '], 'IBJJF')}

    if event_name.value == "ADCC":
        return {"event_name": event_name, "Events": filter_events_by_keyword(upcoming_events()['Upcoming Events '], 'ADCC')}

    if event_name.value == "WNO":
        return {"event_name": event_name, "Events": filter_events_by_keyword(upcoming_events()['Upcoming Events '], 'WNO')}

    return {"event_name": event_name, "Events": "Event Not Found"}


# returns the upcoming headlines listed on the flo-grapplng website
@app.get("/headlines", response_model=dict, summary="latest flo grappling headlines")
async def get_headlines():
    headlines = latest_new_headlines()
    return headlines

# returns the upcoming events listed on the flo-grapplng website
@app.get("/events", response_model=dict, summary="upcoming events")
async def get_events():
    events = upcoming_events()
    return events
