import requests


def request_flights(
        api_key,
        api_host,
        num_people,
        departure_location,
        destination_location,
        departure_date,
        currency):
    """
    This function makes a request to the Flights API to get a list of flights between two locations
    Limit:
        10 requests per minute
    Returns:
        json: Json response from the Flights API
    """

    url = "https://skyscanner44.p.rapidapi.com/search"
    querystring = {"adults": str(num_people),
                   "origin": departure_location,
                   "destination": destination_location,
                   "departureDate": departure_date,
                   "currency": currency}

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": api_host
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    response_status = response.status_code

    response_text = response.text

    return response_text, response_status
