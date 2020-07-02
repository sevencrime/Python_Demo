
from google.protobuf import json_format
from eddidProtobuf import *
import eddidProtobuf.trade_msg_def_pb2 as trade



user = trade.QueryHisDealReq()


dict1 = {
    "session_id" : "${session_id}",
    "account" : "${account}",
    "begin_date" : "2020-05-26 00:00:00",
    "end_date" : "2020-05-26 00:00:00",
    "page_num" : 1,
    "request_num" : 10,
    "start_time_stamp" : 1590422400000
}

for key, value in dict1.items():
    try:
        setattr(user, key, value)

    except ValueError:
        print("字段{} 类型错误, 不支持 {}".format(key, value))

    except Exception as e:
        print(e)
        raise e


print(user)
print(json_format.MessageToJson(user))
