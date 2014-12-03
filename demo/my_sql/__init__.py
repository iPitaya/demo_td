#-*- coding:utf-8 -*-

from sqlalchemy import func
from base import sessionmaker

from base import wodfan_models



wodfan_engine = wodfan_models.get_engine()


Wodfan_DBSession = sessionmaker(expire_on_commit=False)
Wodfan_DBSession.configure(bind=wodfan_engine)


