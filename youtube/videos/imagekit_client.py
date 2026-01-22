import os
from imagekit import ImageKit

def get_imagekit_client():
    return ImageKit()


def upload_image(file_data:bytes, file_name:str, folder: str = "videos"):
    public_key = os.environ.get("IMAGEKIT_PUBLIC_KEY")

    client = get_imagekit_client()

    response = client.files.upload(
        file_data= file_data,
        file_name= file_name,
        folder= folder,
        public_key= public_key
    )  


    return {
        "file_id": response.file_id,
        "url": response.url,
    }