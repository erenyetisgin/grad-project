import cv2
import numpy as np


backsub = cv2.createBackgroundSubtractorMOG2()
capture = cv2.VideoCapture("{video_path}")
blank_image = np.zeros((600,800), np.uint8)
cv2.rectangle(blank_image, (500, 580), (200, 0), (255,255,255), -1)

sayac=0


if capture:

  while True:

    ret, frame = capture.read()

    if ret:
        fgmask = backsub.apply(frame, None, 0.01)
        cv2.line(frame, (200,220), (500,220), (255,255,0), 2)
        cv2.line(frame, (200,240), (500,240), (255,255,0), 2)

        fgmask = cv2.bitwise_and(fgmask, blank_image)
        #kernel = np.ones((5,5), np.uint8)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        img_closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
        img_opening = cv2.morphologyEx(img_closing, cv2.MORPH_OPEN, kernel)
        img_dilation = cv2.dilate(img_opening, kernel, iterations=2)
        #th = img_dilation[img_dilation < 240] =0
        
        
        img_erosion = cv2.erode(fgmask, kernel, iterations=1)
        
        contours, hierarchy = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        try: hierarchy = hierarchy[0]
        except: hierarchy = []
        for contour, hier in zip(contours, hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            
            if w > 40 and h > 40:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                if y > 220 and y < 240:
                    sayac+=1
                    print(sayac)
        
        cv2.putText(frame,"Araba: "+str(sayac), (220, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)

        cv2.imshow("Takip", frame)
        #cv2.imshow("Arka Plan Cikar", fgmask)
        cv2.imshow("Final", img_dilation)
        #cv2.imshow("erosion", img_erosion)
        #cv2.imshow("dilation", img_dilation)
        #cv2.imshow("erosion_fgmask", img_erosion_org)



    key = cv2.waitKey(60)
    if key == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()

