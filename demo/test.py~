#-*- coding:utf-8 -*-
from my_sql import wodfan_models
from my_sql import Wodfan_DBSession
user = wodfan_models('pyach')
class User(user):
    @classmethod
    def get_users_by_ids(cls,user_ids):
        #user_ids = list(set(user_ids))
        dbsession = Wodfan_DBSession()
        user_list = dbsession.query(cls)
	for user1 in user_list:
		print user1._id,user1._name,user1._value
	
        dbsession.commit()
        dbsession.close()
if __name__ == "__main__":
    User.get_users_by_ids(1)
