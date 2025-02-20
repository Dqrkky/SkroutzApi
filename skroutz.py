import cloudscraper


import shared

class Skroutz:
    def __init__(self):
        self.config = {
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
                "X-Requested-With": "XMLHttpRequest"
            }
        }
    def __enter__(self):
        self.shared = shared.Shared()
        self.scraper = cloudscraper.create_scraper()
        return self
    def __exit__(self, exception_type, exception_value, exception_traceback):
        pass
    def getJson(self, config :dict=None):
        if config != None and isinstance(config, dict):  # noqa: E711
            return self.scraper.request(
                *self.shared.convert_json_to_values(
                    config=config
                )
            )
    def search(self, keyphrase :str=None, page :int=1):
        if keyphrase != None and isinstance(keyphrase, str) and \
        page != None and isinstance(page, int):  # noqa: E711
            self.suggest(keyphrase=keyphrase)
            return {
                "method": "get",
                "url": "https://www.skroutz.gr/search",
                "params": {
                    "keyphrase": keyphrase,
                    "page": page
                }
            }
    def suggest(self, keyphrase :str=None):
        if keyphrase != None and isinstance(keyphrase, str):  # noqa: E711
            return {
                "method": "get",
                "url": "https://www.skroutz.gr/suggest",
                "params": {
                    "keyphrase": keyphrase
                }
            }