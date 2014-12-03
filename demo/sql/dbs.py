#-*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import event
from new import classobj


class _Models(object):

    def __init__(self,host,echo=False,pool_recycle=7200,table_names=None,column_prefix='_',schema=None):
        self.models = {}
        self.schema = schema
        self.host = host
        self.echo = echo
        self.pool_recycle = pool_recycle
        self.column_prefix = column_prefix
        self.get_engine()
        self.get_base()
        if table_names is None:
            self.table_names = self.engine.table_names()
        else:
            self.table_names = table_names
        for _tablename in self.table_names:
            _table_name = '{0}'.format(_tablename)
            self.models[_table_name] = self._generate_model(_table_name,self.engine)

    def __call__(self,tablename=None):
        if tablename is None:
            return self.models
        return self.models[tablename]

    def get_engine(self):
        if not hasattr(self,'engine'):
            self.engine = create_engine(self.host,echo=self.echo,pool_recycle=self.pool_recycle)
        return self.engine

    def get_base(self):
        if not hasattr(self,'base'):
            self.base = declarative_base()
        return self.base

    def _generate_model(self,tablename,engine,model_name=None):
        if model_name is None:
            model_name = tablename
        _table = Table(tablename,self.base.metadata,autoload=True,autoload_with=self.engine,schema=self.schema)
        _model = classobj(model_name, (self.base,), {'__table__' : _table, '__mapper_args__' : {'column_prefix' : self.column_prefix}}) 
        return _model

class Models(object):
    _models = {}

    def __new__(cls,host,port,user,passwd,database,tables=None,charset='utf8',echo=False,pool_recycle=7200,column_prefix='_',schema=None):
        if database not in cls._models:
            _connection_str = 'mysql://{0}:{1}@{2}:{3}/{4}?charset={5}'.format(user,passwd,host,port,database,charset)
            cls._models[database] = _Models(_connection_str,echo=echo,pool_recycle=pool_recycle,table_names=tables,column_prefix=column_prefix,schema=schema)
        return cls._models[database]

    @classmethod
    def get_models_by_database(cls,database):
        return cls._models[database]





