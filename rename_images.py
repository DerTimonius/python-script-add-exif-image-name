import os
from PIL import Image, ExifTags

path = (r"<your directory>")

def get_approx_aperture(value):
  valid_apertures = [1.0, 1.1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.5, 2.8, 3.2, 3.5, 4, 4.5, 5, 5.6, 6.3, 7.1, 8, 9, 10, 11, 13, 14, 16, 18, 20, 22, 25, 29, 32, 36, 40]
  for aperture in valid_apertures:
    if value == aperture or value < aperture:
      return aperture

def rename_images():
  for file in os.listdir(path):
    image = Image.open(os.path.join(path, file))
    if image._getexif():
      exif = {
        ExifTags.TAGS[k]: v
        for k, v in image._getexif().items()
        if k in ExifTags.TAGS
      }
      image.close()
      aperture = get_approx_aperture(exif["ApertureValue"])
      focal_length = round(exif["FocalLength"], 0)
      camera = exif["Model"]
      ISO = exif["ISOSpeedRatings"]
      new_filename = f"{focal_length}mm-f{aperture}-ISO{ISO}-{camera}-{file}"
      src = os.path.join(path, file)
      dst = os.path.join(path, new_filename)
      os.rename(src, dst)
      print("Success")

if __name__ == "__main__":
  rename_images()
