# -*- coding: utf-8 -*-

import os
import scrapy


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
        podcast_href = response.xpath("//a[contains(@href,'.mp3')]/@href").extract_first()
        if podcast_href:
            podcast_url = response.urljoin(podcast_href)
            yield {'file_urls': [podcast_url]}
