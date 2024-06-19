#!/usr/bin/env python3
'''
Writing strings to Redis
'''
import redis
import uuid
from typing import Union


class Cache:
    '''
    This class uses method store that takes a data argument
    stores the input data in Redis
    '''
    def __init__(self):
        '''
        initialize and store an instance of Redis client as a
        private variable
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        this method takes a data argument and returns a string
        stores input data in redis using a random key
        '''
        unique_key = str(uuid.uuid4())
        self._redis.set(unique_key, data)
        return unique_key