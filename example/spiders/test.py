from scrapy_redis.spiders import RedisSpider

class TestSpider(RedisSpider):

    name = 'testSpider'

    def parse(self, response):
        pass
