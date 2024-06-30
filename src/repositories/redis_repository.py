from config.config import get_redis_client

r = get_redis_client()

def set_value(key, value):
    r.set(key, value)

def get_value(key):
    return r.get(key)
