from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from example.items import ItcastItem


class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn']

    rules = [
        Rule(LinkExtractor(allow=r"/subject"), 'parse_directory')
        #Rule(LinkExtractor(
         #   restrict_css=('.top-cat', '.sub-cat', '.cat-item')
        #), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        title = response.xpath("//title")
        items = ItcastItem()
        items['title'] = title.xpath('text()').extract()

        h1 = response.xpath("//meta[contains(@name,'keywords')]/@content")
        items['h1'] = h1.extract()
        # h2 = response.xpath("//h2/p/text()").extract()
        h2Str = ''
        h2 = response.xpath("//h2/text()")
        if not h2:
         for content in h2.extract():
            h2Str+=content

        items['h2'] = h2Str

        return items

        #for div in response.css('.title-and-desc'):
         #   yield {

                #'name': div.css('.site-title::text').extract_first(),
                #'description': div.css('.site-descr::text').extract_first().strip(),
                #'link': div.css('a::attr(href)').extract_first(),
           # }
