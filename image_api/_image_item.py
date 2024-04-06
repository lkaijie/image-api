class ImageItem:
    # def __init__(self, url, title = "", source = "", width = "", height = ""):
    #     self.url = url
    #     self.title = title
    #     self.source = source
    #     self.width = width
    #     self.height = height
    def __init__(self, dict: dict) -> None:
        print(dict)
        try:
            self.url = dict["url"]
            self.title = dict["title"]
            self.width = dict["width"]
            self.height = dict["height"]
            self.format = dict["format"]
        except KeyError:
            pass
        pass