# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from cassandra.cluster import Cluster, PlainTextAuthProvider
from cassandra.query import SimpleStatement



class CityIntroPipeline:
    def open_spider(self, spider):
        # Connect to the Cassandra cluster          
        self.auth_provider = PlainTextAuthProvider('cassandra', 'cassandra')
        self.cluster = Cluster(['cassandra'], port=9042, auth_provider=self.auth_provider)
        self.session = self.cluster.connect()
        # self.session.set_keyspace('datn') 
        self.session.execute('USE datn')

    def close_spider(self, spider):
        # Close the Cassandra connection
        self.session.shutdown()
        self.cluster.shutdown()

    # def process_item(self, item, spider):
    #     # Insert the item data into the Cassandra table
    #     query = """
    #          INSERT INTO city_intro (city_id, city_name, country_name, city_image, title, intro, activity)
    #          VALUES (?, ?, ?, ?, ?, ?, ?)
    #      """
    #     prepared_statement = self.session.prepare(query)
    #     self.session.execute(prepared_statement, (
    #         item['city_id'], item['city_name'], item['country_name'],
    #         item['city_image'], item['title'], item['intro'], item['activity']
    #     ))

    def process_item(self, item, spider):
        # Insert the item data into the Cassandra table
        query = """
             INSERT INTO city_intro (city_id, city_name, country_name, city_image, title, intro, activity)
             VALUES (%s, %s, %s, %s, %s, %s, %s)
         """
        statement = SimpleStatement(query, consistency_level=1)
        self.session.execute(statement, (
            item['city_id'],
            item['city_name'],
            item['country_name'],
            item['city_image'],
            item['title'],
            item['intro'],
            item['activity']
        ))

        return item
