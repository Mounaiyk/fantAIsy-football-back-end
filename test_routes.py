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
    # def test_stats/(self, api):
    #     resp = api.get('/')
    #     assert resp.status == '200 OK'
    # def test_home(self, api):
    #     resp = api.get('/')
    #     assert resp.status == '200 OK'
    # def test_home(self, api):
    #     resp = api.get('/')
    #     assert resp.status == '200 OK'