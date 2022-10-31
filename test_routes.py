import json
import pytest
import conftest
import app

class TestAPIcase():
    def test_home(self, api):
        resp = api.get('/')
        assert resp.status == '200 OK'
    def test_allstats(self, api):
        resp = api.get('/allstats')
        assert resp.status == '200 OK'
    def test_stats_for_player(self, api):
        resp = api.get('/stats/Granit Xhaka')
        assert resp.status == '200 OK'
    def test_team_stats(self, api):
        resp = api.get('/teams/Manchester United F.C.')
        assert resp.status == '200 OK'
    def test_user_stats(self, api):
        resp = api.get('/userplayer/5883591')
        assert resp.status == '200 OK'
    # def test_home(self, api):
    #     data = {'email': 'brad.neve@gmail.com', 'password': 'Futureproof#1', 'userID': '5883591'}
    #     resp = api.post('/getuserteam', data = data)
    #     assert resp.status == '201 OK'