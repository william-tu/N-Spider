# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MongoPipeline(object):
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=crawler.settings.get('MONGO_URI'),
#             mongo_db=crawler.settings.get('MONGO_DATABASE')
#         )
#
#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#
#     def close_spider(self, spider):
#         self.client.close()
#
#     def process_item(self, item, spider):
#         collection_name = item.__class__.__name__
#         if self.db[collection_name].find({"data_id": item["data_id"]}).count():
#             return item
#         self.db[collection_name].insert(dict(item))
#         return item


class MysqlPipeline(object):
    def __init__(self, mysql_config):
        self.mysql_config = mysql_config
        self.connection = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_config=crawler.settings.get("MYSQL_CONFIG")
        )

    def open_spider(self, spider):
        import pymysql.cursors
        self.connection = pymysql.connect(cursorclass=pymysql.cursors.DictCursor, **self.mysql_config)

    def process_item(self, item, spider):
        with self.connection.cursor() as cursor:
            cursor.execute("select `data_id` from `article` where `data_id`=%s", (item.get("data_id")))
            if cursor.fetchone():
                return
            sql = "INSERT INTO `article` (`data_id`, `title`, `content`, `message_url`, `image_url`, `add_time`, `source_from`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (item.get("data_id"), item.get("title"), item.get("content"), item.get("message_url"),
                                 item.get("image_url"), item.get("add_time"), item.get("source_from")))
            self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
