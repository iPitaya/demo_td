#-*- coding:utf-8 -*-
PYES_HOST_CONFIG = [
    ("thrift", "192.168.1.42", "5571"),
    #("thrift", "192.168.1.11", "9500"),
    #("thrift", "192.168.1.19", "9500"),
    #("thrift", "192.168.1.16", "9500"),
]

MXYC_USER_ID = 100
db_pool_recycle = 60

MYSQL_CONFIG = dict(
    host = '192.168.1.108',
    port = 3307,
    user = 'editor',
    passwd = 'x7PfEb9bor74oqpF9dE8IWB8p',
    charset = 'utf8',
)

MYSQL_DATABASES_TABLES = dict(
    wodfan = ['user','authorization_user','user_prize', \
              'refused_user','forbidden_ip','forbidden_user', \
              'operation_log','navigator','editor_name'],
    forum = ['threads','topic','bankuai','top_threads','report',
             'thread_recommend','classuser','staruser','tasks','star_user_type'],
    youku = ['show','show_star'],
    dau = ['channel','dau_data','platform_data', \
           'pv_uv_channel_data','taobao_channel','taobao_click_data'],
    droplist = ['droplist'],
    comment = ['thread_comment','thread_comment_imgs', 'star_comment', 'topic_comment'],
    upload = ['image'],
    message = ['official_msg'],
    showlist = ['showlist_flow'],
)

MYSQL_20_CONFIG = dict(
    host = '192.168.1.19',
    port = 3306,
    user = 'editor',#'siren',
    passwd = 'x7PfEb9bor74oqpF9dE8IWB8p',#'DCB01C3C1F197C2C0F7B2153522AD6E0768B9B1D',
    charset = 'utf8',
)

MYSQL_20_DATABASES_TABLES = dict(
    siren = ['event'],
    statistics = ['forum_threads','forum_statistics','forum_province','thread_pv'],
)

MYSQL_169_CONFIG = dict(
    host = '192.168.1.108',
    port = 3307,
    user = 'editor',
    passwd = 'x7PfEb9bor74oqpF9dE8IWB8p',
    charset = 'utf8',
)

MYSQL_169_DATABASES_TABLES = dict(
    collection = ['thread'],
)




