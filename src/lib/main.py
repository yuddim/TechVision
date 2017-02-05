
import cv2

from slidingWindow.slidingWindow import SlidingWindow

if __name__ == '__main__':
    print '-----start-------'

    x = SlidingWindow()
    y = x.sliding_windows(10)
    print y
    print '------end--------'
