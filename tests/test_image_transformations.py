import os
import shutil
from tempfile import mkdtemp
from unittest import mock

from PIL import Image

from image_client import ImageManipulator, IMAGE_FILTERS

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SRC_IMAGE = os.path.join(BASE_DIR, 'tests', 'fixtures', 'invisible_bike.jpg')


class TestImageTransformations:

    def setup(self):
        self.tmp_dir = mkdtemp()
        self.input_file = os.path.join(self.tmp_dir, 'test_image.jpg')
        shutil.copy(SRC_IMAGE, self.input_file)

    def teardown(self):
        shutil.rmtree(self.tmp_dir)

    def test_compress_image(self):
        expected_output_file = os.path.join(self.tmp_dir, 'test_image_compress_50.jpg')

        ImageManipulator(self.input_file).compress(50)

        outputs = os.listdir(self.tmp_dir)
        input_size = os.path.getsize(self.input_file)
        output_size = os.path.getsize(expected_output_file)

        assert sorted(outputs) == sorted([os.path.basename(expected_output_file), os.path.basename(self.input_file)])
        assert input_size > output_size

    def test_rotate_image(self):
        expected_output_file = os.path.join(self.tmp_dir, 'test_image_rotate_90.jpg')
        input_size = Image.open(self.input_file).size
        rotated_size = tuple(reversed(input_size))

        ImageManipulator(self.input_file).rotate(90)

        output_size = Image.open(expected_output_file).size
        outputs = os.listdir(self.tmp_dir)

        assert sorted(outputs) == sorted([os.path.basename(expected_output_file), os.path.basename(self.input_file)])
        assert output_size == rotated_size

    def test_generate_thumbnail(self):
        expected_output_file = os.path.join(self.tmp_dir, 'test_image_thumbnail_90.jpg')
        thumbnail_size = (90, mock.ANY)

        ImageManipulator(self.input_file).thumbnail(90)

        outputs = os.listdir(self.tmp_dir)

        assert sorted(outputs) == sorted([os.path.basename(expected_output_file), os.path.basename(self.input_file)])
        assert Image.open(expected_output_file).size == thumbnail_size

    def test_filter_image(self):
        for filter in IMAGE_FILTERS:
            expected_output_file = os.path.join(self.tmp_dir, 'test_image_filter_{}.jpg'.format(filter))

            ImageManipulator(self.input_file).filter(filter)

            outputs = os.listdir(self.tmp_dir)

            assert os.path.basename(self.input_file) in outputs
            assert os.path.basename(expected_output_file) in outputs
