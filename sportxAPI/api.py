#Created By: Jon Kolman
import requests

def get_active_markets():
	return requests.get('https://app.api.sportx.bet/markets/active').json()

def get_popular_markets():
	return requests.get('https://app.api.sportx.bet/markets/popular').json()

def get_all_leagues():
	return requests.get('https://app.api.sportx.bet/leagues').json()

def get_active_leagues():
	return requests.get('https://app.api.sportx.bet/leagues/active').json()

def get_all_sports():
	return requests.get('https://app.api.sportx.bet/sports').json()


def get_all_fixtures_for_league(leagueId):
	return requests.get('https://app.api.sportx.bet/fixture/active?leagueId=%s`').json() % (leagueId)

def get_meta_data():
	return requests.get('https://app.api.sportx.bet/metadata').json()

def get_active_orders():
	return requests.get('https://app.api.sportx.bet/orders').json()



