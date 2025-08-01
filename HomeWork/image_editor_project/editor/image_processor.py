import cv2 as cv


class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv.imread(image_path)
        if self.image is None:
            raise ValueError("Could not load image from the specified path.")
        self.original_image = self.image.copy()

    def adjust_contrast_brightness(self, alpha=1.0, beta=0):
        adjusted = cv.convertScaleAbs(self.image, alpha=alpha, beta=beta)
        self.image = adjusted

    def draw_line(self, start_point, end_point, color, thickness):
        cv.line(self.image, start_point, end_point, color, thickness)

    def draw_rectangle(self, top_left, bottom_right, color, thickness):
        cv.rectangle(self.image, top_left, bottom_right, color, thickness)

    def save_image(self, output_path):
        cv.imwrite(output_path, self.image)
        return True

    def get_image_dimensions(self):
        height, width, _ = self.image.shape
        return width, height
