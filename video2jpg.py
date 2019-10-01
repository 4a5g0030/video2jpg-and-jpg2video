import cv2

video = cv2.VideoCapture('test_data/video/test.mp4')
success, image = video.read()
count = 0
while success:
    filename = 'test_data/image/' + str(count).zfill(3) + '.jpg'
    cv2.imwrite(filename, image)
    print(count)
    count += 1
    video.set(cv2.CAP_PROP_POS_MSEC,(count * 125))
    success, image = video.read()
