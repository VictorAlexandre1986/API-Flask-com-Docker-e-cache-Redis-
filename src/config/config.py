import redis

def get_redis_client():
    return redis.Redis(host='redis', port=6379, db=0)