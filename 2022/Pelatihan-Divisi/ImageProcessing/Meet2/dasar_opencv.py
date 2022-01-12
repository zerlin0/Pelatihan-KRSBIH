import numpy as np
import cv2 as cv

# cap = cv.VideoCapture(0) # Wecam Utama
kamera = cv.VideoCapture(0) # Wecam Utama

#
# Cek Kondisi Kamera
# if not kamera.isOpened():
#     print("Cannot open camera")
#     exit()
#
def resizeGambar(frame,faktor = 50):
    lebar = frame.shape[1]
    tinggi = frame.shape[0]

    # percent by which the image is resized
    scale_percent = faktor

    # calculate the 50 percent of original dimensions
    width = int(lebar * scale_percent / 100)
    height = int(tinggi * scale_percent / 100)

    # dsize
    dsize = (width, height)
    frame_resize = cv.resize(frame, dsize)
    return frame_resize


while True:
    # Capture frame-by-frame
    kondisi, frame = kamera.read()
    # if frame is read correctly ret is True
    if not kondisi:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame_kecil = resizeGambar(frame, 30)
    cv.imshow('frame bgr', frame_kecil)

    frame_filter = cv.bilateralFilter(frame_kecil, 10, 70, 70)

    frame_gray = cv.cvtColor(frame_filter, cv.COLOR_BGR2GRAY)
    cv.imshow('frame gray', frame_gray)

    edges = cv.Canny(frame_filter, 100, 100)
    cv.imshow('canny edge',edges )

    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
kamera.release()
cv.destroyAllWindows()
