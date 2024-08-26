from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Base URL for the BallDontLie API
BASE_URL = "https://api.balldontlie.io/v1"

@app.route('/', methods=['GET', 'POST'])
def index():
    player_stats = None
    
    if request.method == 'POST':
        player_name = request.form['prompt']
        player_stats = get_player_stats(player_name)
    
    return render_template('index.html', player_stats=player_stats)

def get_player_stats(player_name):
    # Split the player name into first and last name for the search query
    name_parts = player_name.split()
    first_name = name_parts[0]
    last_name = name_parts[1] if len(name_parts) > 1 else ''

    # Fetch player information
    search_url = f"{BASE_URL}/players"
    response = requests.get(search_url,headers = {"Authorization" : "07f8b008-98d4-465d-b340-79459f1ac5b6"})
    player_id = 0
    API_Data = response.json()
    for player in API_Data.get('data',[]):
        if player['first_name'] == first_name and player['last_name'] == last_name:
            player_id = player['id']
            break
    
    ##print(player_id)
    if response.status_code == 200 :
        ##if first_name in response.json()['first_name'] and last_name in response.json()['last_name']:
            ##player_id = response.json()[]  # Get the first matching player
        

        # Fetch player stats by player ID
        ##player_id = 15
        stats_url = f"{BASE_URL}/season_averages?season=2023&player_ids[]={player_id}"
        stats_response = requests.get(stats_url,headers = {"Authorization" : "07f8b008-98d4-465d-b340-79459f1ac5b6"})
        print(stats_response.json())
        
        if stats_response.status_code == 200:

            stats_data = stats_response.json()['data'][0]
            
            player_stats = {
                'name': f"{first_name} {last_name}",
                'points': stats_data['pts'],
                'rebounds': stats_data['reb'],
                'assists': stats_data['ast']
            }
            return player_stats
        else:
            return {'error': 'Player stats not found for the current season.'}
    else:
        return {'error': 'Player not found. Please check the name and try again.'}

if __name__ == '__main__':
    app.run(debug=True)
