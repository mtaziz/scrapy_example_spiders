# -*- coding: utf-8 -*-

# Scrapy settings for stadlistan_sweden project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'stadlistan_sweden'

SPIDER_MODULES = ['stadlistan_sweden.spiders']
NEWSPIDER_MODULE = 'stadlistan_sweden.spiders'
DOWNLOAD_DELAY=10

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]
###{{{ProxyMiddleware(privoxy)
# HTTP_PROXY = 'https://127.0.0.1:8123' ###Popilo Proxy Config###
HTTP_PROXY = 'https://127.0.0.1:8118'	###{Privoxy Proxy Config}###
DOWNLOADER_MIDDLEWARES = {
     'stadlistan_sweden.middlewares.RandomUserAgentMiddleware': 400,
     'stadlistan_sweden.middlewares.ProxyMiddleware': 410,
     'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None
    # Disable compression middleware, so the actual HTML pages are cached
}
###}}}


###{{{Feed Exporters to force CSV in ordered
FEED_EXPORTERS = {
    'csv': 'stadlistan_sweden.exporters.StadlistanItemExporter'
}
###}}}

###{{{ Item Pipelines
# ITEM_PIPELINES = { 'scrapy.pipelines.images.ImagesPipeline': 600
	
# }
# ITEM_PIPELINES = {
# 	'lawsociety.pipelines.Pipeline':600,
# 	}
###}}}

FIELDS_TO_EXPORT = [
	'Source_Urls', 
	'Company_Name',
	'Company_Website',
	'Email', 
	# 'SRA_ID', 
	# 'SRA_Status', 
	# 'Association_At', 
	# 'Telephone', 
	# 'Email', 
	# 'Practice_Area', 
	# 'Language_Spoken'
	]

# CSV_DELIMITER = '\t'
# CSV_JOIN_MULTIVALUED = '|'

# COOKIES_ENABLED=False
# HTTPCACHE_ENABLED=True
# HTTPCACHE_EXPIRATION_SECS=84600
# HTTPCACHE_DIR='httpcache'
# HTTPCACHE_ENABLED=True
# HTTPCACHE_EXPIRATION_SECS=84600
# HTTPCACHE_DIR='httpcache'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lawsociety (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lawsociety.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lawsociety.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'lawsociety.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED=True
# HTTPCACHE_EXPIRATION_SECS=84600
# HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
