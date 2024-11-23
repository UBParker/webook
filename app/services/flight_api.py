import requests

def fetch_flights(query_params):
    # Example integration with a flight API (Amadeus, Skyscanner, etc.)
    # TO-DO: Need to find one I can get without a company
    response = requests.get("https://api.example.com/flights", params=query_params)
    return response.json()
