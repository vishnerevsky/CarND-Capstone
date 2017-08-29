from styx_msgs.msg import TrafficLight
import numpy as np
import cv2

class TLClassifier(object):
    def __init__(self):
        self.pixel_threshold = 40 # Thresholding value for colored pixels
        
        # Manually set boundaries for colors
        self.boundaries = [
            ([80, 80, 170], [120, 120, 255]), # Red
        ]

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)
            0 for red, 4 for green/yellow/none
        """

        # Set default state
        state = TrafficLight.UNKNOWN

        for (lower, upper) in self.boundaries:
            lower = np.array(lower, dtype = "uint8")
            upper = np.array(upper, dtype = "uint8")

            # Count boundary colors in image
            mask = cv2.inRange(image, lower, upper)
            color_detection = cv2.countNonZero(mask)

            # Threshold detected red colors
            if color_detection > self.pixel_threshold:
                state = TrafficLight.RED

        return state
