import scrapy
from urllib.parse import urlparse

class WebCrawler(scrapy.Spider):
    name = "web_crawler"
    seed_url = 'https://presidencyuniversity.in/'
    max_pages = 10
    max_depth = 3
    allowed_domains = [urlparse(seed_url).netloc]  # Restrict crawling to the domain of the seed URL

    def start_requests(self):
        self.pages_crawled = 0
        yield scrapy.Request(self.seed_url, self.parse, meta={'depth': 1, 'max_pages': self.max_pages, 'max_depth': self.max_depth})

    def parse(self, response):
        max_pages = response.meta['max_pages']
        max_depth = response.meta['max_depth']

        if self.pages_crawled < max_pages and response.meta['depth'] <= max_depth:
            self.pages_crawled += 1
            yield {
                'url': response.url,
                'title': response.css('title::text').get(),
                'content': ' '.join(response.css('body *::text').getall()),  # Get all text within the body tag
            }

            # Follow links to the next pages
            for next_page in response.css('a::attr(href)').getall():
                next_page_url = response.urljoin(next_page)
                # Check if the URL is within the allowed domain
                if urlparse(next_page_url).netloc in self.allowed_domains:
                    yield response.follow(next_page_url, self.parse, meta={'depth': response.meta['depth'] + 1, 'max_pages': max_pages, 'max_depth': max_depth})

