import unittest
import cv2
import image
class TestData(unittest.TestCase):

    def test_text(self):
        img = "quote_inspiration_motivation_138489_1920x1080.jpg"
        img = image.checkFormat(img)
        img = image.resize(img, hight=720, width=500)
        thresh = image.Threshold(img)
        data = image.loadData(thresh)

        self.assertIn('visit' , data)

if __name__ == "__main__":
    unittest.main()
