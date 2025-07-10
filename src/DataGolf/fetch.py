import requests
from typing import Any, Union
from config import APIKey
from utils import normalize_stat_category


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

def fetch_player_skill_app(file_format="json", period="l12"):
    """Access DataGolf api and return player skill approach specific data.
        Period: 
        'l24' - last 24 months, 'l12' - last 12 months 'ytd' - year to date
    """ 
    url = f"https://feeds.datagolf.com/preds/approach-skill?period={period}&file_format={file_format}&key={APIKey}"
    data = fetch(url)

    total_data = []
    # normalize data
    for player in data['data']:
        normal_data = {}
        for cat in player:
            # Parse stat category with '_' as delimiter
            cat_list = cat.split('_')
            # Check no bounds errors
            if len(cat_list) < 3:
                continue
            # Select distance category e.g. 100_150
            cat_type = cat_list[0] + "_" + cat_list[1]
            stat_type = "_".join(cat_list[3:])
            full_cat = cat_type + "_" + cat_list[2]
            # Pass normal_data dictionary in to be normalizeed
            normalize_stat_category(normal_data, stat_type, player, cat, full_cat)
        normal_data['player_name'] = player['player_name']
        normal_data['dg_id'] = player['dg_id']
        total_data.append(normal_data)
    return total_data

if __name__ == "__main__":
    #fetch_player_list("json")
    fetch_player_skill_app()