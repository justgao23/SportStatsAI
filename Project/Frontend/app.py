from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    player_stats = None
    
    if request.method == 'POST':
        player_name = request.form['player_name']
        # For now, we'll just return a mock response
        player_stats = {
            'name': player_name,
            'points': 25.4,
            'rebounds': 7.2,
            'assists': 6.3
        }
    
    return render_template('index.html', player_stats=player_stats)

if __name__ == '__main__':
    app.run(debug=True)
