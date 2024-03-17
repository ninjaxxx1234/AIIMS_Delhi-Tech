import cv2
import easyocr
import os.path as osp
import glob
import cv2
import numpy as np
import torch
import RRDBNet_arch as arch
import pandas as pd
import time

vid = cv2.VideoCapture(0)

reader = easyocr.Reader(['en'], gpu=True)

interval = 2
itr = 0

limit = False
user_metric = input("Enter the metric you wish to keep track of (RR/VTe): ")
user_thresh = int(input("Enter the THRESHOLD for which you ought to be alerted: "))
blob = 4
bbox_regions = {
    "VTe": [[562, 238], [616, 238], [616, 272], [562, 272]],
    "RR": [[581, 81], [625, 81], [625, 120], [581, 120]]
}
while not limit:
    ret, frame = vid.read()
    #cv2.imshow("frame", frame)
    output_resized = frame
    results = reader.readtext(output_resized)
    res_df = pd.DataFrame(results, columns=['bbox', 'text', 'conf'])
    filtered_df = res_df[res_df['conf'] >= 0.55]
    filtered_results = [item for item in results if item[2] >= 0.55]
    resp_region = [[520, 120], [630, 124], [630, 160], [586, 156]]
    resp_x_min, resp_x_max = 580, 630
    resp_y_min, resp_y_max = 124, 156
    for detection in filtered_results:

        bbox = detection[0]
        text = detection[1]

        x_min, y_min = [int(val) for val in bbox[0]]
        x_max, y_max = [int(val) for val in bbox[2]]
        if (x_min in range(bbox_regions[user_metric][0][0]-blob, bbox_regions[user_metric][0][0]+blob) and
                x_max in range(bbox_regions[user_metric][2][0]-blob, bbox_regions[user_metric][2][0]+blob) and
                y_min in range(bbox_regions[user_metric][0][1]-blob, bbox_regions[user_metric][0][1]+blob) and
                y_max in range(bbox_regions[user_metric][2][1]-blob, bbox_regions[user_metric][2][1]+blob)):
            val = int(text)
            print(val)
            if val >= user_thresh:
                limit = True
                break

        cv2.rectangle(output_resized, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)


        cv2.putText(output_resized, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.rectangle(output_resized, (bbox_regions[user_metric][0][0]-blob, bbox_regions[user_metric][0][1]-blob), (bbox_regions[user_metric][2][0]+blob, bbox_regions[user_metric][2][1]+blob), (0, 255, 255), 2)
    cv2.imshow("Output_FINAL", output_resized)
    #if itr%2==0:
        #print(filtered_df)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    itr += 1
cv2.destroyAllWindows()

if limit:
    red_image = cv2.imread('red-color.png')
    cv2.imshow("CODE RED", red_image)
    cv2.waitKey(0)
    time.sleep(10)

vid.release()
cv2.destroyAllWindows()
