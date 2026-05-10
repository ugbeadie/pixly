from imagekitio import ImageKit

from app.core.config import IMAGEKIT_PRIVATE_KEY, IMAGEKIT_URL

imagekit = ImageKit(private_key=IMAGEKIT_PRIVATE_KEY)

URL_ENDPOINT = IMAGEKIT_URL
