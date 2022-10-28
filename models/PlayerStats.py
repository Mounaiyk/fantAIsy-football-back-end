
from app import db

class Player_stats(db.Model):
    id = db.Column(db.Integer)
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
    takes_corners = db.Column("takes_corners", db.Boolean)
    takes_free_kicks = db.Column("takes_free_kicks", db.Boolean)
    takes_penalites = db.Column("takes_penalites", db.Boolean)
    points_per_game = db.Column("points_per_game", db.Integer())

    def __init__(self, id, name, goals, assists, clean_sheets, chance_of_playing, points_per_game, selected_by_percentage, team, total_points, transfers_in, transfers_out, transfers_in_this_round, transfers_out_this_round, minutes, goals_conceded, own_goals, penalties_saved, penalties_missed, yellow_cards, red_cards, bonus_points, saves, influence, creativity, threat, ict_index, takes_corners, takes_free_kicks, takes_penalties, points_per_game ):
        self.id = id
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
        self.points_per_game = points_per_game

