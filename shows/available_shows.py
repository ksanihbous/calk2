import re
import os.path

class Show(object):
    def __init__(self, name, seasons, episodes):
        self.name = name
        self.seasons = seasons
        self.episodes = episodes

def get_all_shows():
    list_of_shows = []
    filepath = os.path.join(os.path.dirname('data'), 'list_of_shows.csv')
    try:
        with open(filepath) as f:
            content = f.readlines()
            for line in content:
                shows = line.split(',')
                list_of_shows.append(shows)
    except:
        raise  FileNotFoundError('list_of_shows not found or corrupt')

def get_all_seasons(show_name):
    list_of_shows = get_all_shows()
    for s in list_of_shows:
        if show_name == s:
            return 'Match'
    else:
        return 'Show not in list'

def get_all_episodes(show_name, season):
    return None

def get_latest_episode(show_name):
    return None

