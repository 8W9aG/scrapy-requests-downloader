"""The middleware for scrapy-requests-downloader."""
import scrapy
import requests


class RequestsDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=scrapy.signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=scrapy.signals.spider_closed)
        return s

    def should_process_request(self, request: scrapy.Request, spider: scrapy.Spider) -> bool:
        """Whether we should process a request."""
        return request.meta.get("requests_enabled", spider.settings.get("REQUESTS_ENABLED", False))

    def perform_requests_request(self, request: scrapy.Request) -> scrapy.http.Response:
        """Perform a requests request using a scrapy request."""
        method_function = getattr(requests, request.method.lower())
        response = method_function(
            request.url,
            headers={x.decode(): request.headers[x].decode() for x in request.headers},
            cookies=request.cookies,
            data=request.body
        )
        return scrapy.http.Response(
            response.url,
            status=response.status_code,
            headers=response.headers,
            body=response.content,
            request=request
        )

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        if self.should_process_request(request, spider):
            return self.perform_requests_request(request)
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        pass

    def spider_closed(self, spider):
        pass
