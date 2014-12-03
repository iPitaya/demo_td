#-*- coding:utf-8 -*-

from sqlalchemy import func
from models.base import sessionmaker

from models.base import forum_models
from models.base import wodfan_models
from models.base import youku_models
from models.base import dau_models
from models.base import droplist_models
from models.base import comment_models
from models.base import upload_models
from models.base import statistics_models
from models.base import siren_models
from models.base import collection_models
from models.base import message_models
from models.base import showlist_models

forum_engine = forum_models.get_engine()
wodfan_engine = wodfan_models.get_engine()
youku_engine = youku_models.get_engine()
dau_engine = dau_models.get_engine()
droplist_engine = droplist_models.get_engine()
comment_engine = comment_models.get_engine()
upload_engine = upload_models.get_engine()
statistics_engine = statistics_models.get_engine()
siren_engine = siren_models.get_engine()
collection_engine = collection_models.get_engine()
message_engine = message_models.get_engine()
showlist_engine = showlist_models.get_engine()

Forum_DBSession = sessionmaker(expire_on_commit=False)
Forum_DBSession.configure(bind=forum_engine)

Wodfan_DBSession = sessionmaker(expire_on_commit=False)
Wodfan_DBSession.configure(bind=wodfan_engine)

Youku_DBSession = sessionmaker(expire_on_commit=False)
Youku_DBSession.configure(bind=youku_engine)

Dau_DBSession = sessionmaker(expire_on_commit=False)
Dau_DBSession.configure(bind=dau_engine)

Droplist_DBSession = sessionmaker(expire_on_commit=False)
Droplist_DBSession.configure(bind=droplist_engine)

Comment_DBSession = sessionmaker(expire_on_commit=False)
Comment_DBSession.configure(bind=comment_engine)

Upload_DBSession = sessionmaker(expire_on_commit=False)
Upload_DBSession.configure(bind=upload_engine)

Statistics_DBSession = sessionmaker(expire_on_commit=False)
Statistics_DBSession.configure(bind=statistics_engine)

Siren_DBSession = sessionmaker(expire_on_commit=False)
Siren_DBSession.configure(bind=siren_engine)

Collection_DBSession = sessionmaker(expire_on_commit=False)
Collection_DBSession.configure(bind=collection_engine)

Message_DBSession = sessionmaker(expire_on_commit=False)
Message_DBSession.configure(bind=message_engine)

Showlist_DBSession = sessionmaker(expire_on_commit=False)
Showlist_DBSession.configure(bind=showlist_engine)

from .model_utils.tools import DateTime

from .wodfan.navigator import Navigator
from .wodfan.wodfan import User
from .wodfan.wodfan import Authorization_user
from .wodfan.wodfan import Wodfan_DBSession
from .wodfan.user_prize import User_prize
from .wodfan.refused_user import Refused_user
from .wodfan.forbidden_ip import Forbidden_ip
from .wodfan.forbidden_user import Forbidden_user
from .wodfan.editor_name import EditorName

#from .forum.report import Report
from .forum.report import Report
from .forum.topic import Topic
from .forum.bankuai import Bankuai
from .forum.classuser import ClassUser
from .forum.staruser import StarUser
from .forum.threads import Threads
from .forum.threads2 import Threads2
from .forum.top_threads import TopThreads
from .forum.thread_recommend import ThreadRecommend
from .forum.postcomments import PostComments
from .forum.tasks import Task
from .forum.star_user_type import StarUserType

from .youku.show import Show
from .youku.show_star import Show_star

from .dau.channel import Channel
from .dau.taobao_channel import TaobaoChannel
from .dau.platform_data import PlatformData
from .dau.pv_uv_channel_data import PvUvChannelData
from .dau.taobao_click_data import TaobaoClickData
from .dau.dau_data import DauData

from .droplist.droplist import Droplist
from .upload.image import UploadImage

from .comment.thread_comment_imgs import ThreadCommentImgs
from .comment.thread_comment import ThreadComment
from .comment.topic_comment import TopicComment
from .comment.star_comment import StarComment

from .message.message_content import MessageContent
from .message.official_message import OfficialMsg
from .wodfan.operation_log import OperationLog
LOG_TYPE = OperationLog
LOG = OperationLog.log
# LOG(op_user_id,typename,type_id,**params)
#params { user_id, bankuai_id, thread_id, comment_id }

from config import MXYC_USER_ID
from .sensitive.sensitive import Sensitive
from .statistics.forum_threads import ForumThreads
from .sensitive.audit import Audit

from .siren.event import Event
from .collection.thread_collect import ThreadCollect

from .showlist.showlist_flow import ShowlistFlow


