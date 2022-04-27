# scrapy-requests-downloader

<a href="https://pypi.org/project/scrapy-requests-downloader/">
    <img alt="PyPi" src="https://img.shields.io/pypi/v/scrapy-requests-downloader">
</a>

Scrapy middleware with requests support as an alternative to Twisted calls.

## Dependencies :globe_with_meridians:

* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [Scrapy 2.4.0](https://scrapy.org/)
* [requests 2.27.1](https://docs.python-requests.org/en/latest/)

## Installation :inbox_tray:

This is a python package hosted on pypi, so to install simply run the following command:

`pip install scrapy-requests-downloader`

## Settings

### REQUESTS_ENABLED

Whether the requests middle is used to process any request (defaults to false).

Meta field to enable/disable this per request is: `requests_enabled`

## Usage example :eyes:

In order to use this plugin simply add the following settings and substitute your variables:

```py
DOWNLOADER_MIDDLEWARES = {
    "requestsmiddleware.middleware.RequestsDownloaderMiddleware": 632
}
```

In order to use it as a downloader you can add the following to your settings:

```py
REQUESTS_ENABLED = True
```

This will make every request use requests for a response.

## License :memo:

The project is available under the [MIT License](LICENSE).
