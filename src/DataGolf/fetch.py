import os
import json
import requests
from typing import Any, Union
from config import APIKey

def fetch (url) :
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    else:
        data = None
        print("Request failed: ", response.status_code)
    return data

def fetch_raw_scoring_data(tour: str, event_id: Union [int, str], year:int, file_format: str="json") -> Any:
    """Access DataGolf api and return raw scoring data from specified event."""

    url = f"https://feeds.datagolf.com/historical-raw-data/rounds?tour={tour}&event_id={event_id}&year={year}&file_format={file_format}&key={APIKey}"
    data = fetch(url)
    return data

def fetch_player_list(file_format="json") -> Any:
    """Access DataGolf api and return player list and IDs."""
    url = f"https://feeds.datagolf.com/get-player-list?file_format={file_format}&key={APIKey}"
    data = fetch(url)
    return data

def fetch_player_skill_ratings(file_format="json") -> Any:
    """Access DataGolf api and return player skill ratings."""
    # Can swap value argument for 'rank' if necessary 
    url = f"https://feeds.datagolf.com/preds/skill-ratings?display=value&file_format={file_format}&key={APIKey}"
    data = fetch(url)
    return data['players']

if __name__ == "__main__":
    #fetch_player_list("json")
    fetch_player_skill_ratings("json")