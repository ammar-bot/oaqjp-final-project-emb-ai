from emotion_detection import emotion_detector
import unittest


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_analyzer(self):
        
        result_1 = emotion_detector('I am glad this happened')
        result_2 = emotion_detector('I am really mad about this')
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        result_4 = emotion_detector('I am so sad about this')
        result_5 = emotion_detector('I am really afraid that this will happen')


unittest.main()