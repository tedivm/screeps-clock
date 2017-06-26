
import screepsapi.screepsapi as screepsapi
from screeps_clock import app
from screeps_clock.services.cache import cache

time_factor = 1


def getCurrentTime():
    return getCurrentTick() * time_factor


@cache.cache(expire=3)
def getCurrentTick():
    user = app.config['API_USERNAME']
    password = app.config['API_PASSWORD']
    api = screepsapi.API(user, password)
    return api.time()
