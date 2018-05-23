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
            yield scrapy.Request(episode_url, callback=self.download_mp3)

    def download_mp3(self, response):
        podcast_href = response.xpath("//a[contains(@href,'.mp3')]/@href").extract_first()
        if podcast_href:
            file_path = self.mp3_file_path(podcast_href)

            if not os.path.exists(file_path):
                podcast_url = response.urljoin(podcast_href)
                yield scrapy.Request(podcast_url, callback=self.save_file)

    def save_file(self, response):
        file_path = self.mp3_file_path(response.url)
        with open(file_path, 'wb') as f:
            f.write(response.body)

    def mp3_file_path(self, url):
        return os.path.join(self.settings['FILES_STORE'], url.split('/')[-1])
