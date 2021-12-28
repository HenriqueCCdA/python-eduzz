from urllib.parse import urljoin, urlparse

from eduzz.sessions.base import BaseSession


class BaseUrlSession(BaseSession):
    """Taken from https://github.com/requests/toolbelt/"""

    def __init__(self, base_url="", **kwargs):
        self.base_url = base_url
        super(BaseUrlSession, self).__init__(**kwargs)

    @staticmethod
    def is_absolute(url):
        return bool(urlparse(url).netloc)

    def ensure_absolute_url(self, url):
        if self.is_absolute(url):
            return url

        return urljoin(self.base_url, url)

    def prepare_request(self, request):
        """Prepare the request after generating the complete URL."""
        request.url = self.ensure_absolute_url(request.url)
        return super(BaseUrlSession, self).prepare_request(request)
