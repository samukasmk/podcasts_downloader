# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


# absolute_url solution by Frank:
# https://stackoverflow.com/questions/48874341/python-scrapy-get-absolute-url-using-input-processor

def absolute_url(url, loader_context):
    return loader_context['response'].urljoin(url)


class PodcastMP3Item(scrapy.Item):
    file_urls = scrapy.Field(input_processor=MapCompose(absolute_url))
