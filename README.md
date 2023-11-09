# FLO-GRAPPLING FastAPI Service

Welcome to the FLO-GRAPPLING FastAPI service! This service provides a RESTful API to access information about athletes, latest news headlines, and upcoming events related to FLO Grappling, all containerized with Docker for easy deployment.

## Features

- **Athletes Endpoint**: Get a list of current athletes featured on FLO Grappling.
- **Events Endpoint**: Search for events by type (e.g., ADCC, WNO, IBJJF).
- **Headlines Endpoint**: Receive the latest FLO Grappling headlines.
- **Upcoming Events Endpoint**: Find out about upcoming events in the world of grappling
##
Endpoints
GET /athletes
Returns a list of all the current FLO athletes.
##
GET /events/{event_name}
Find all the events by a specific type. Replace {event_name} with ADCC, WNO, or IBJJF.
##
GET /headlines
Fetch the latest FLO grappling headlines.
##
GET /events
Retrieve information on upcoming events.
##
Contributing
We welcome contributions from the community. If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.
