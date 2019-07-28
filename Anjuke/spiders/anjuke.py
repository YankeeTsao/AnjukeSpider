# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Anjuke.items import AnjukeSZItem

class AnjukeSpider(CrawlSpider):
    name = 'anjuke_sz'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://shenzhen.anjuke.com/sale/p1']

    rules = [
            Rule(LinkExtractor(allow=("https://shenzhen\.anjuke\.com/sale/p\d{1,}"))),
            Rule(LinkExtractor(allow=("https://shenzhen\.anjuke\.com/prop/view/A\d{1,}")), callback='parse_item', follow=False)
    ]

    def get_bd_item(self, response):
        bd_nodes = {}
#       二手房信息页面经过javascript处理，禁用javascript时信息处理div[4]启用javascript时信息被移动到div[3]，scrapy默认是不运行javascript的所以需要使用禁用javascript时的路径才能获取信息。
        bd_nodes["bd_name"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[1]/div[2]/a/text()')
        bd_nodes["bd_location"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[4]/div[2]/p')
        bd_nodes["bd_buildTime"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[7]/div[2]/text()')
        bd_nodes["bd_type"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[10]/div[2]/text()')
        bd_nodes["bd_property"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[13]/div[2]/text()')
        bd_nodes["bd_layout"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[2]/div[2]/text()')
        bd_nodes["bd_size"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[5]/div[2]/text()')
        bd_nodes["bd_direction"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[8]/div[2]/text()')
        bd_nodes["bd_floor"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[11]/div[2]/text()')
        bd_nodes["bd_lift"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[14]/div[2]/text()')
        bd_nodes["bd_averagePrice"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[3]/div[2]/text()')
        bd_nodes["bd_totalPrice"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[1]/div[1]/span[1]/em//text()')
        bd_nodes["bd_oneHand"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[18]/div[2]/text()')
        bd_nodes["bd_decoration"] = response.xpath('//*[@id="content"]/div[4]/div[1]/div[3]/div/div[1]/ul/li[12]/div[2]/text()')

        bd_item = self.struct_bd_item(bd_nodes)
        return bd_item

    def struct_bd_item(self, bd_nodes):
        bd_item = AnjukeSZItem()
        if bd_nodes['bd_name']:
            bd_item['bd_name'] = bd_nodes['bd_name'].extract()[0].strip()
        else:
            bd_item['bd_name'] = ''
        if bd_nodes['bd_location']:
            bd_item['bd_location'] = bd_nodes['bd_location'].xpath('string(.)').extract()[0].strip().replace(' ','').replace('\n','')
        else:
            bd_item['bd_location'] = ''
        if bd_nodes['bd_buildTime']:
            bd_item['bd_buildTime'] = bd_nodes['bd_buildTime'].extract()[0].strip()
        else:
            bd_item['bd_buildTime'] = ''
        if bd_nodes['bd_type']:
            bd_item['bd_type'] = bd_nodes['bd_type'].extract()[0].strip()
        else:
            bd_item['bd_type'] = ''
        if bd_nodes['bd_property']:
            bd_item['bd_property'] = bd_nodes['bd_property'].extract()[0].strip()
        else:
            bd_item['bd_property'] = ''
        if bd_nodes['bd_layout']:
            bd_item['bd_layout'] = bd_nodes['bd_layout'].extract()[0].strip().replace('\t', '').replace('\n', '')
        else:
            bd_item['bd_layout'] = ''
        if bd_nodes['bd_size']:
            bd_item['bd_size'] = bd_nodes['bd_size'].extract()[0].strip()
        else:
            bd_item['bd_size'] = ''
        if bd_nodes['bd_direction']:
            bd_item['bd_direction'] = bd_nodes['bd_direction'].extract()[0].strip()
        else:
            bd_item['bd_direction'] = ''
        if bd_nodes['bd_floor']:
            bd_item['bd_floor'] = bd_nodes['bd_floor'].extract()[0].strip()
        else:
            bd_item['bd_floor'] = ''
        if bd_nodes['bd_lift']:
            bd_item['bd_lift'] = bd_nodes['bd_lift'].extract()[0].strip()
        else:
            bd_item['bd_lift'] = ''
        if bd_nodes['bd_averagePrice']:
            bd_item['bd_averagePrice'] = bd_nodes['bd_averagePrice'].extract()[0].strip().replace(' ', '')
        else:
            bd_item['bd_averagePrice'] = ''
        if bd_nodes['bd_totalPrice']:
            bd_item['bd_totalPrice'] = bd_nodes['bd_totalPrice'].extract()[0].strip()
        else:
            bd_item['bd_totalPrice'] = ''
        if bd_nodes['bd_oneHand']:
            bd_item['bd_oneHand'] = bd_nodes['bd_oneHand'].extract()[0].strip()
        else:
            bd_item['bd_oneHand'] = ''
        if bd_nodes['bd_decoration']:
            bd_item['bd_decoration'] = bd_nodes['bd_decoration'].extract()[0].strip()
        else:
            bd_item['bd_decoration'] = ''
        return bd_item

    def parse_item(self, response):
        bd_item = self.get_bd_item(response)
        bd_item['bd_url'] = response.url
        return bd_item
