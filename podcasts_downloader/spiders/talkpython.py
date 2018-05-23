# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from podcasts_downloader.items import PodcastMP3Item

class TalkpythonSpider(scrapy.Spider):
    name = 'talkpython'
    allowed_domains = ['talkpython.fm']
    start_urls = ['https://talkpython.fm/episodes/all']

    def parse(self, response):
        episode_hrefs = response.xpath('//td/a[contains(@href,"episodes/show")]//@href').extract()

        for episode_href in episode_hrefs:
            episode_url = response.urljoin(episode_href)
            yield scrapy.Request(episode_url, callback=self.parse_mp3_links)

    def parse_mp3_links(self, response):
        url_loader = ItemLoader(item=PodcastMP3Item(), response=response)
        url_loader.add_xpath('file_urls', '//a[contains(@href,".mp3")]/@href')
        return url_loader.load_item()