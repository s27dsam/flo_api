import requests
from bs4 import BeautifulSoup


def flo_athletes():
    # The URL of the page you want to scrape
    url = 'https://www.flograppling.com/people'
    # Perform the HTTP request to get the page content
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        #     # Find the elements that contain the athlete's name
        athlete_elements = soup.find_all('h2',
                                         class_='avatar-container__primary-text mb-0 pt-1 pt-md-0 headline w-100 text-truncate text-center text-wrap text-line-clamp-2 ng-star-inserted')
        # Extract and print each athlete's name
        athletes = []
        for athlete in athlete_elements:
            athletes.append(athlete.get_text(strip=True))
        return {"Flo Athletes": athletes}
    else:
        return "Failed to retrieve the webpage"


def upcoming_events():
    # The URL of the page you want to scrape
    url = 'https://www.flograppling.com/signup'

    # Perform the HTTP request to get the page content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all event items
        event_items = soup.find_all('div', class_='list-item-wrapper')  # Replace with the correct class or tag

        # Extract the date, time, and name of each event
        events = []
        for item in event_items:
            date = item.find('h4', class_='event-date').get_text(strip=True) if item.find('h4',
                                                                                          class_='event-date') else 'Date not found'
            time = item.find('p', class_='event-footnote').get_text(strip=True) if item.find('p',
                                                                                             class_='event-footnote') else 'Time not found'
            event_name = item.find('h4', class_='event-title').get_text(strip=True) if item.find('h4',
                                                                                                 class_='event-title') else 'Event name not found'

            events.append(f"Date: {date}, Time: {time}, Event: {event_name}")
        return {'Upcoming Events ': events}

    else:
        print("Failed to retrieve the webpage")


def latest_new_headlines():
    # The URL of the page you want to scrape
    url = 'https://www.flograppling.com/articles'
    # Perform the HTTP request to get the page content
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        #     # Find the elements that contain the athlete's name
        news = soup.find_all('h5',
                             class_='h5 mb-1 flex-grow-0 color-900 mobile-header-resize text-line-clamp-2 apply-text-hover')
        # Extract and print each athlete's name
        headlines = []
        for headline in news:
            headlines.append(headline.get_text(strip=True))
        return {"Flo News Headlines": headlines}
    else:
        return "Failed to retrieve the webpage"


def filter_events_by_keyword(events: list, keyword: str) -> list:
    # Filter the events that contain the keyword, case insensitive
    keyword_lower = keyword.lower()
    filtered_events = [event for event in events if keyword_lower in event.lower()]
    return filtered_events




