#-*- coding:utf-8 -*-
import functools
from utils.dbs import Models
from utils.dbs import sessionmaker
from config import MYSQL_CONFIG,MYSQL_DATABASES_TABLES,db_pool_recycle
from config import MYSQL_20_CONFIG,MYSQL_20_DATABASES_TABLES
from config import MYSQL_169_CONFIG,MYSQL_169_DATABASES_TABLES
                                                                                                                      
def generate_models(mysql_config,mysql_databases_tables,database_name,echo=False,column_prefix='_'):                                    
    _host     = mysql_config['host']
    _port     = mysql_config['port']
    _user     = mysql_config['user']
    _passwd   = mysql_config['passwd']
    _database = database_name
    _charset  = mysql_config['charset']
    _tables   = mysql_databases_tables[_database]
    _models   = Models( host         = _host,
                         port         = _port,
                         user         = _user,
                         passwd       = _passwd,
                         database     = _database,
                         tables       = _tables,
                         charset      = _charset,
                         echo         = echo,
                         pool_recycle = db_pool_recycle,
                         column_prefix = column_prefix,
                         schema = _database
                       )
    return _models 

generate_models_online = functools.partial(generate_models,MYSQL_CONFIG,MYSQL_DATABASES_TABLES)
generate_models_20 = functools.partial(generate_models,MYSQL_20_CONFIG,MYSQL_20_DATABASES_TABLES)
generate_models_169 = functools.partial(generate_models,MYSQL_169_CONFIG,MYSQL_169_DATABASES_TABLES)

wodfan_models = generate_models_online('wodfan',echo=False)
forum_models = generate_models_online('forum',echo=False)
youku_models = generate_models_online('youku',echo=False)
dau_models = generate_models_online('dau',echo=False)
droplist_models = generate_models_online('droplist',echo=False)
comment_models = generate_models_online('comment',echo=False)
upload_models = generate_models_online('upload',echo=False)
message_models = generate_models_online('message',echo=True)
showlist_models = generate_models_online('showlist',echo=True)

siren_models = generate_models_20('siren',echo=True)
statistics_models = generate_models_20('statistics',echo=True)

collection_models = generate_models_169('collection',echo=False)

