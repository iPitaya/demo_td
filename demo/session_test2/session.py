# -*- coding: utf-8 -*-

import os, time
import uuid

class Session(object):
    _prefix = "_session:"
    _id = None
    _skip = ['_redis','_request','_id']
    def __init__(self,request):
        self._redis = request.redis
        self._request = request
        #init session id
        id = request.get_secure_cookie('sessionid')
        if id and self._redis.exists(id):
            self._id = id

    def init_session(self):
        """初始化"""
        if not self._id:
            self._id = self.generate_session_id()
            self._request.set_secure_cookie('sessionid',self._id)
        #延期sessionid过期时间
        self._redis.hset(self._id,'lastActive',time.time())
        self._redis.expire(self._id, 10) # session_maxlifetime -> 10s

    def generate_session_id(self):
        """Generate a random id for session"""
        sessionid = self._prefix + uuid.uuid1().hex
        assert(not self._redis.exists(sessionid))
        return sessionid

    def __getattr__(self, name):
        if self._id:
            return self._redis.hget(self._id,name)
        return None

    def __setattr__(self, name, value):
        if not name in self._skip:
            self.init_session()
            self._redis.hset(self._id,name,value)
            self._redis.expire(self._id, 10) # session_maxlifetime -> 10s
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if not name in self._skip:
            return self._redis.hdel(self._id,name)
        object.__delattr__(self, name)
