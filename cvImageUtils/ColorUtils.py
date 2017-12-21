import numpy as np
import cv2


class ColorUtils:

    @staticmethod
    def rgb_color_seperation(image):
        """
        takes a color image, and splits it into three channels.

        :param image: color image
        :return: rgb values
        """
        height, width, channels = image.shape
        if channels != 3:
            raise ValueError

        b, g, r = cv2.split(image)  # break image into colors in RGB Space
        return r, g, b

    @staticmethod
    def hsv_color_sep(image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        return h, s, v


    @staticmethod
    def color_sep_image(image, method):

        height, width, channels = image.shape
        if method == 'rgb':
            a, b, c = ColorUtils.rgb_color_seperation(image)
        else: # hsv
            a, b, c = ColorUtils.hsv_color_sep(image)

        rgb_split = np.empty([height, width * 3, 3], 'uint8')
        rgb_split[:, 0:width] = cv2.merge([a, a, a])
        rgb_split[:, width:width * 2] = cv2.merge([b, b, b])
        rgb_split[:, width * 2:width * 3] = cv2.merge([b, b, b])

        return rgb_split

    @staticmethod
    def convert_rbg_to_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    @staticmethod
    def convert_rgb_to_rgba(image):
        height, width, channels = image.shape
        if channels != 3:
            raise ValueError

        return cv2.merge((image[:, :, 0],
                          image[:, :, 1],
                          image[:, :, 2],
                          np.ones([height, width]).astype(np.uint8) * 255))

    @staticmethod
    def basic_threshold(image, threshold):
        """
        Convert an image to black and white, based on a single threshold value

        :param image: The image to adjust (should be black and white)
        :param threshold: the value to use to split the pixels
        :return: the image adjusted
        """

        ret, thresh_basic = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
        return thresh_basic

    @staticmethod
    def adaptive_threshold(image, block_size):
        """
        Convert an image to black and white, based on a single threshold value

        :param image: The image to adjust (should be black and white)
        :param block_size: the neighborhood to use for threshold (must be odd!)
        :return: the image adjusted
        """

        # make sure the block_size is odd
        if block_size % 2 == 0:
            raise ValueError("block size must be odd")

        thres_adapt = cv2.adaptiveThreshold(image,
                                            255,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY,
                                            block_size,
                                            1)

        return thres_adapt
