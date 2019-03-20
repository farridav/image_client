import os

from PIL import Image, ImageFilter

IMAGE_FILTER_MAP = {
    'BLUR': ImageFilter.BLUR,
    'CONTOUR': ImageFilter.CONTOUR,
    'DETAIL': ImageFilter.DETAIL,
    'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
    'EDGE_ENHANCE_MORE': ImageFilter.EDGE_ENHANCE_MORE,
    'EMBOSS': ImageFilter.EMBOSS,
    'FIND_EDGES': ImageFilter.FIND_EDGES,
    'SHARPEN': ImageFilter.SHARPEN,
    'SMOOTH': ImageFilter.SMOOTH,
    'SMOOTH_MORE': ImageFilter.SMOOTH_MORE,
}

IMAGE_FILTERS = [_ for _ in IMAGE_FILTER_MAP.keys()]


class ImageManipulator:

    def __init__(self, filename):
        self.image = Image.open(filename)

        filename, ext = os.path.splitext(filename)
        self.filename = filename
        self.ext = ext
        self.out_dir = os.path.dirname(filename)

    def _get_output_name(self, operation, parameter):
        new_filename = os.path.join(self.out_dir, "{file}_{operation}_{param}{ext}".format(
            file=self.filename, operation=operation, ext=self.ext, param=parameter
        ))
        return new_filename

    def rotate(self, angle):
        self.image = self.image.rotate(angle, expand=1)
        output = self._get_output_name('rotate', angle)
        self.image.save(output, "JPEG")

        return output

    def thumbnail(self, size):
        self.image.thumbnail((size, size), Image.ANTIALIAS)
        output = self._get_output_name('thumbnail', size)
        self.image.save(output, "JPEG")

        return output

    def compress(self, quality):
        output = self._get_output_name('compress', quality)
        self.image.save(output, "JPEG", quality=quality, optimize=True)

        return output

    def filter(self, filter):
        output = self._get_output_name('filter', filter)
        self.image = self.image.filter(IMAGE_FILTER_MAP.get(filter))
        self.image.save(output, "JPEG")

        return output

    def process(self, operation, *args):
        mapping = {
            'compress': 'compress',
            'rotate': 'rotate',
            'filter': 'filter',
            'thumbnail': 'thumbnail'
        }

        return getattr(self, mapping[operation])(*args)
