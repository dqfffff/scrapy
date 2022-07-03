# Scrapy settings for job project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'job'

SPIDER_MODULES = ['job.spiders']
NEWSPIDER_MODULE = 'job.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'DEBUG'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
temp = 'lastCity=101270100; sid=sem_pz_bdpc_dasou_title; __zp_seo_uuid__=c843f3ee-3a64-4dcc-b0bf-48177684fa34; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1656726422; wd_guid=2549f028-f6cf-40dc-9c1a-056bc8dd39ad; historyState=state; _bl_uid=64ldw5t33qk8U061b0q9jnvvIg9e; wt2=DAm6_KxehzgZXwi2JTgeuiJZb-_dg7x4eyR5i1crL6pcu_D3j5_jdkGHlmhXY_Xp7kKXEHGwiJaR1iqQJzRIChg~~; wbg=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1656750334; __c=1656726422; __l=r=https://www.baidu.com/other.php?sc.0600000-R26gd0oAcI5NneYCIF4gpK6x9_OQTaPpn4WQfxTyx3AvXBDYeeJXZf7NBTE-r0DmLpNeYhArfHFhziOKWokFDcGOku_Cn8NSR7O9FJu78_6fMXJt1OCdO1BCMvVVTOXdowl3x0kdfQIys654n1C51S8LKlxh3Jusx6oKmkRDCo0_9xexiSuTvF_VvyG08scsWFQu4kjGsxYao9pjsasE.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1TsKdTvNzgLw4TARqn0K9u7qYXgK-5Hn0IvqzujdBULP10ZFWIWYs0ZNzU7qGujYkPHnvrj64P1fs0Addgv-b5HDYPWcsnWD10AdxpyfqnHDvnWn1PHn0UgwsU7qGujYknW6zP6KsI-qGujYs0A-bm1dcfbD0TA-b5Hc30APGujYznWm0mLFW5HnsnjDk&dt=1656726418&wd=boss&tpl=tpl_12826_27888_0&l=1536889740&us=linkVersion%3D1%26compPath%3D10036.0-10032.0%26label%3D%25E4%25B8%25BB%25E6%25A0%2587%25E9%25A2%2598%26linkType%3D%26linkText%3DBOSS%25E7%259B%25B4%25E8%2581%2598%25E2%2580%2594%25E2%2580%2594%25E6%2589%25BE%25E5%25B7%25A5%25E4%25BD%259C%25EF%25BC%258C%25E4%25B8%258ABOSS%25E7%259B%25B4%25E8%2581%2598%25EF%25BC%258C&l=/www.zhipin.com/web/geek/job?query=&s=3&g=/www.zhipin.com/chengdu/?sid=sem_pz_bdpc_dasou_title&friend_source=0&s=3&friend_source=0; __a=37250023.1656726422..1656726422.12.1.12.12; __zp_stoken__=f5a9dYUQWejVVPHc6fm0RXB4QIGktDws8LjotXG1rKnENGh4jexANFXdudkssACZ2LSYJeFJ6ZQRzCVAYNzcoQ0EmV0cvD3xlGG0RVwx0O31jQWYAVhx6XlxCYzYnOkkWbx87BiAbEA1tOiw=; acw_tc=0b328f3616568038653704196e011d27f3ecef7d302359a60ff34e394785fc; geek_zp_token=V1RN4hF-b92F1vVtRvyhsQKS-45D3VzC0~'
cookies = {data.split('=')[0]: data.split('=')[-1] for data in temp.split('; ')}
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'referer': 'https://www.zhipin.com/',
    # 'cookie': cookies,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'job.middlewares.JobSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'job.middlewares.JobDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'job.pipelines.JobPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
