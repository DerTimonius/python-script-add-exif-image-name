# Add Exif data to your image file names

This little Python script will add certain Exif data (aperture, focal length and camera model) to the image file name.

## Examples

_DSC0508.jpg &rarr; 28mm-f5-ISO100-ILCE-7M3-_DSC0508.jpg
_DSC0033.jpg &rarr; 283mm-f6.3-ISO400-ILCE-7M3-_DSC0033.jpg


## Usage

To use it yourself, the following steps are necessary:

```
git clone https://github.com/DerTimonius/python-script-add-exif-image-name
cd python-script-add-exif-image-name
```

If it not installed on your machine already, install the Python Image Library:

```
pip install pillow
```

Change the path inside of the `rename_images.py` file.

```python
path = (r"<Your directory path>")
```
It could look something like this:
```python
path = (r"C:\Users\DerTimonius\Pictures\2022\Croatia")
```

Make sure to keep the ``r`` and the quotation marks.

In your terminal you now just have to write:
```bash
python rename_images.py
```
Now all the files in your directory will be renamed if there is EXIF data stored with them!

