from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from werkzeug import exceptions
import requests
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///player_stats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

class Player_stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column("player_id", db.Integer())
    name = db.Column("name", db.String())
    goals = db.Column("goals", db.Integer())
    assists = db.Column("assists", db.Integer())
    clean_sheets = db.Column("clean_sheets", db.Integer())
    chance_of_playing = db.Column("chance_of_playing", db.Integer())
    points_per_game = db.Column("points_per_game", db.Integer())
    selected_by_percentage = db.Column("selected_by_percentage", db.Integer())
    team = db.Column("team", db.Integer())
    total_points = db.Column("total_points", db.Integer())
    transfers_in = db.Column("transfers_in", db.Integer())
    transfers_out = db.Column("transfers_out", db.Integer())
    transfers_in_this_round = db.Column("transfers_in_this_round", db.Integer())
    transfers_out_this_round = db.Column("transfers_out_this_round", db.Integer())
    minutes = db.Column("minutes", db.Integer())
    goals_conceded = db.Column("goals_conceded", db.Integer())
    own_goals = db.Column("own_goals", db.Integer())
    penalties_saved = db.Column("penalties_saved", db.Integer())
    penalties_missed = db.Column("penalties_missed", db.Integer())
    yellow_cards = db.Column("yellow_cards", db.Integer())
    red_cards = db.Column("red_cards", db.Integer())
    bonus_points = db.Column("bonus_points", db.Integer())
    saves = db.Column("saves", db.Integer())
    influence = db.Column("influence", db.Integer())
    creativity = db.Column("creativity", db.Integer())
    threat = db.Column("threat", db.Integer())
    ict_index = db.Column("ict_index", db.Integer())
    takes_corners = db.Column("takes_corners", db.Integer())
    takes_free_kicks = db.Column("takes_free_kicks", db.Integer())
    takes_penalties = db.Column("takes_penalties", db.Integer())

    def __init__(self, player_id, name, goals, assists, clean_sheets, chance_of_playing, points_per_game, selected_by_percentage, team, total_points, transfers_in, transfers_out, transfers_in_this_round, transfers_out_this_round, minutes, goals_conceded, own_goals, penalties_saved, penalties_missed, yellow_cards, red_cards, bonus_points, saves, influence, creativity, threat, ict_index, takes_corners, takes_free_kicks, takes_penalties ):
        self.player_id = player_id
        self.name = name
        self.goals = goals
        self.assists = assists
        self.clean_sheets = clean_sheets
        self.chance_of_playing = chance_of_playing
        self.points_per_game = points_per_game
        self.selected_by_percentage = selected_by_percentage
        self.team = team
        self.total_points = total_points
        self.transfers_in = transfers_in
        self.transfers_out = transfers_out
        self.transfers_in_this_round = transfers_in_this_round
        self.transfers_out_this_round = transfers_out_this_round
        self.minutes = minutes
        self.goals_conceded = goals_conceded
        self.own_goals = own_goals
        self.penalties_saved = penalties_saved
        self.penalties_missed = penalties_missed
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.bonus_points = bonus_points
        self.saves = saves
        self.influence = influence
        self.creativity = creativity
        self.threat = threat
        self.ict_index = ict_index
        self.takes_corners = takes_corners
        self.takes_free_kicks = takes_free_kicks
        self.takes_penalties = takes_penalties

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
   

def fetch_all_stats():
    resp = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    data = resp.json()
    for p in data["elements"]:
    
        teams =["Arsenal", "Aston Villa FC","Bournemouth AFC","Brentford", "Brighton & Hove Albion", "Chelsea", "Crystal Palace", "Everton FC", "Fulham", "Leicester City FC", "Leeds United", "Liverpool FC", "Manchester City FC", "Manchester United FC", "Newcastle United", "Nottingham Forest", "Southampton FC","Tottenham Hotspur FC","West Ham United","Wolverhampton Wanderers"   ]

        player_id = p["id"]
        name = p["first_name"] + " " + p["second_name"]
        goals = p["goals_scored"]
        assists = p["assists"]
        clean_sheets = p["clean_sheets"]
        chance_of_playing = p["chance_of_playing_this_round"]
        points_per_game = p["points_per_game"]
        selected_by_percentage = p["selected_by_percent"]
        team = teams[p["team"]-1]     
        total_points = p["total_points"]
        transfers_in = p["transfers_in"]
        transfers_out = p["transfers_out"]
        transfers_in_this_round = p["transfers_in_event"]
        transfers_out_this_round = p["transfers_out_event"]
        minutes = p["minutes"]
        goals_conceded = p["goals_conceded"]
        own_goals = p["own_goals"]
        penalties_saved = p["penalties_saved"]
        penalties_missed = p["penalties_missed"]
        yellow_cards = p["yellow_cards"]
        red_cards = p["red_cards"]
        bonus_points = p["bonus"]
        saves = p["saves"]
        influence = p["influence"]
        creativity = p["creativity"]
        threat = p["threat"]
        ict_index = p["ict_index"]
        takes_corners = p["corners_and_indirect_freekicks_order"] 
        takes_free_kicks = p["direct_freekicks_order"] 
        takes_penalties = p["penalties_order"]

        player = Player_stats(player_id, name, goals, assists, clean_sheets, chance_of_playing, points_per_game, selected_by_percentage, team, total_points, transfers_in, transfers_out, transfers_in_this_round, transfers_out_this_round, minutes, goals_conceded, own_goals, penalties_saved, penalties_missed, yellow_cards, red_cards, bonus_points, saves, influence, creativity, threat, ict_index, takes_corners, takes_free_kicks, takes_penalties)

        db.session.add(player)
        db.session.commit()

with app.app_context():
    db.create_all()
    # fetch_all_stats()

@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/allstats')
def get_all_stats():
    data = Player_stats.query.all()
    list =[]
    for p in data:
        del p.__dict__["_sa_instance_state"]
        list.append(p.__dict__)
    return jsonify(list)

@app.route('/stats/<str>')
def get_player_stats(str):
    data = Player_stats.query.filter_by(name = str)
    list =[]
    for p in data:
        del p.__dict__["_sa_instance_state"]
        list.append(p.__dict__)
    return jsonify(list)

if __name__ == "__main__":
    app.run(debug=True)