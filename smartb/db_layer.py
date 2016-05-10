import pymongo
from smartbathroom.settings import conf
class db_layer:
    def __init__(self,coll_name):
        self.conn = pymongo.MongoClient()
        self.coll = (self.conn[conf['dbname']])[coll_name]

    def get_data(self,cond):
        cur = self.coll.find(cond)
        l = []
        for i in cur:
            l.append(i)
        return l

    #expect records as list of records
    def set_data(self,record):
        self.coll.insert_one(record)


    def set_realtime_data(self,record):
        rec = self.get_data({"tag":"real_time_data"})
        record['tag'] = "real_time_data"
        if rec:
            self.update_data({"_id":rec[0]["_id"]}, {"$set":record})
        else:
            self.set_data(record)


    def update_data(self,query, condition):
        self.coll.update_one(query, condition)

    def remove(self,cond):
        self.coll.remove(cond)