"""
    vendor for fake the client
"""
from . import header


class _Chrome:
    class pc:
        @staticmethod
        def header():
            return header.create().agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")

    class mobile:
        @staticmethod
        def header():
            return header.create().agent("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Mobile Safari/537.36")


# vendor of default client
default = _Chrome

# vendor of chrome client
chrome = _Chrome
