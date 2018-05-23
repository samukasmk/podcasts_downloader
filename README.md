# podcasts_downloader
Scraper tool to download podcasts files some lovely sites as TalkPython.fm. 


## Setup and Run

### Clone project

```sh
git clone https://github.com/samukasmk/podcasts_downloader.git
cd podcasts_downloader
```

### Create virtualenv

```sh
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configure folder to store mp3 files of podcasts

Edit bellow attribute in file podcasts_downloader/settings.py 

```
FILES_STORE = '/tmp/podcasts_mp3'
```

### Run scraper of talkpython.fm

```sh
scrapy crawl talkpython
```

### Check downloaded files

![Downloaded mp3 files](https://raw.githubusercontent.com/samukasmk/podcasts_downloader/master/docs/imgs/ls-downloaded-files.png)