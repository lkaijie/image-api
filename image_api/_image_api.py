import json
from image_api._base import _Base
import image_api.config as config
# from _image_item import ImageItem
from image_api._image_item import ImageItem

# low = 640 x 420
# mid = 1280 x 720
# high = 1920 x 1080


class ImageApi(_Base):
    
    def __init__(self, timeout: int) -> None:
        super().__init__(timeout)
        self.image_endpoint = config.IMAGE_ENDPOINT
    # hidden methods here
    def _extract_images(self, soup) -> dict:
        pass

    def search(self, query, quality = "" , count = 10, width: int = None, height: int = None) -> dict:
        # handling custom image quality here
        if quality == "low":
            quality = " 640x420"
        elif quality == "mid":
            quality = " 1280x720"
        elif quality == "high":
            quality = " 1920x1080"
        
        if width and height:
            quality = f"{width}x{height}"
        print(self.image_endpoint + query + quality)
        soup = self._parse_url(self.image_endpoint + query + quality)

        # this is every single item li
        # imgs = []
        imgs: list[ImageItem] = []
        for item in soup.find_all("li", attrs={"data-idx": True}):
            item = item.find("a", attrs={"class": "iusc"})
            img_url = "null"
            img_item = ImageItem()
            if item:
                try:
                    img_url = json.loads(item["m"])
                    img_url = img_url["murl"]
                    img_item.url = img_url
                    
                except KeyError:

                    pass
            # imgs.append(img_url)
            imgs.append(img_item)
        # return imgs[:count]
        return imgs
            
        
if __name__ == "__main__":
    api = ImageApi(5)
    api.search("frieren")
    print("done")