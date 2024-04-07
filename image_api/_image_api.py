import json
from image_api._base import _Base
import image_api.config as config
# from _image_item import ImageItem
# from image_api._image_item import ImageItem
from image_api._image_item import ImageItem

# low = 640 x 420
# mid = 1280 x 720
# high = 1920 x 1080


class ImageApi(_Base):
    
    # Image Quality
    quality_map = {
        "low": " 640x420p",
        "mid": " 1280x720p",
        "high": " 1920x1080p"
    }

    
    def __init__(self, timeout: int) -> None:
        super().__init__(timeout)
        self.image_endpoint = config.IMAGE_ENDPOINT
        
    # hidden methods here
    def _extract_images(self, soup) -> dict:
        pass

    def search(self, query, quality = "" , count = 10, width: int = None, height: int = None) -> dict:
        # handle image quality
        quality = self.quality_map.get(quality, "")
        
        if width and height:
            quality = f"{width}x{height}p"
        print(self.image_endpoint + query + quality)
        soup = self._parse_url(self.image_endpoint + query + quality)

        # this is every single item li
        # imgs = []
        imgs: list[ImageItem] = []
        
        for item in soup.find_all("li", attrs={"data-idx": True}):
            # testing = item
            # print(testing)
            img_item = item.find("a", attrs={"class": "iusc"})
            name_layer = item.find("a", attrs={"class": "inflnk"})
            # img_dimensions = img_item.find("span", attrs={"class": "nowrap"}).text.split("·")
            img_dimensions = item.find("span", attrs={"class": "nowrap"}).text.split("·")
            img_url = "null"
            img_width = "null"
            img_height = "null"
            img_format = "null"
            img_title = "null"
            img_dict = {}

            if img_item:
                img_url = json.loads(img_item["m"])
            
            if img_dimensions:
                img_width, img_height = img_dimensions[0].split("x")
                img_format = img_dimensions[1].strip()
                
            if name_layer:
                img_title = name_layer["aria-label"]
                
            
            img_dict['url'] = img_url["murl"]
            img_dict['title'] = img_title
            img_dict['width'] = img_width
            img_dict['height'] = img_height
            img_dict['format'] = img_format
            imgs.append(ImageItem(img_dict))
        return imgs
            
            
            if img_item:
                try:
                    img_name = name_layer["aria-label"]
                    w_h = img_dimensions[0].split("x")
                    img_width = w_h[0].strip()
                    img_height = w_h[1].strip()
                    img_format = img_dimensions[1].strip()
                    img_url = json.loads(img_item["m"])

                    img_dict['url'] = img_url["murl"]
                    img_dict['title'] = img_name
                    img_dict['width'] = img_width
                    img_dict['height'] = img_height
                    # img_format = img_format
                    img_dict['format'] = img_format
                except KeyError:
                    pass
            if img_url != "null":
                imgs.append(ImageItem(img_dict))
        return imgs
            
        
if __name__ == "__main__":
    api = ImageApi(5)
    api.search("frieren")
    print("done")