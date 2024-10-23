from scrapy.crawler import CrawlerProcess
from quotes_scraper.spiders.quotes_spider import QuotesSpider

process = CrawlerProcess(settings={
    "FEEDS": {
        "quotes.json": {"format": "json"},
    },
})

process.crawl(QuotesSpider)
process.start()