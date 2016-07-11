# -*- coding: utf-8 -*-

# Scrapy settings for app project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'app'

SPIDER_MODULES = ['app.spiders']
NEWSPIDER_MODULE = 'app.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'app (+http://www.yourdomain.com)'

# ITEM_PIPELINES = [
#   'scrapy_mongodb.MongoDBPipeline',
# ]
#
# MONGODB_URI = 'mongodb://127.0.0.1:27017'
# MONGODB_DATABASE = 'scrapy'
# MONGODB_COLLECTION = 'google'
#
# EXTENSIONS = {'scrapy.contrib.feedexport.FeedExporter': None}