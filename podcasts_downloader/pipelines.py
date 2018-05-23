# -*- coding: utf-8 -*-

import os
import re
from scrapy.pipelines.files import FilesPipeline
from podcasts_downloader.settings import FILES_STORE

starts_with_id = re.compile('^[0-9]+')


class DownloadMP3FilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        # creates download folder if it does not exists
        podcast_domain = request.url.split('/')[2]
        os.makedirs(os.path.join(FILES_STORE, podcast_domain), exist_ok=True)

        # get file name with postcast id if it does not have
        podcast_file = request.url.split('/')[-1]
        if not starts_with_id.match(podcast_file):
            podcast_id = request.url.split('/')[-2]
            podcast_file = f'{podcast_id}-{podcast_file}'

        return os.path.join(podcast_domain, podcast_file)
