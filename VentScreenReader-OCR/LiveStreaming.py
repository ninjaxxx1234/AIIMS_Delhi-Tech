
import easyocr
import cv2
import pandas as pd
import time
from tkinter import simpledialog

vid = cv2.VideoCapture(0)

reader = easyocr.Reader(['en'], gpu=True)

blob = 4
bbox_regions = {
    "VTe": [[562, 238], [616, 238], [616, 272], [562, 272]],
    "RR": [[581, 81], [625, 81], [625, 120], [581, 120]]
}

def get_user_inputs():
    user_metric = simpledialog.askstring("Input", "Enter the metric you wish to keep track of (RR/VTe): ")
    user_thresh = simpledialog.askinteger("Input", "Enter the THRESHOLD for which you ought to be alerted: ")
    return user_metric, user_thresh

def process_video(user_metric, user_thresh):
    interval = 2
    itr = 0
    limit = False
    while not limit:
        ret, frame = vid.read()
        output_resized = frame
        results = reader.readtext(output_resized)
        res_df = pd.DataFrame(results, columns=['bbox', 'text', 'conf'])
        filtered_df = res_df[res_df['conf'] >= 0.55]
        filtered_results = [item for item in results if item[2] >= 0.55]
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
                if val >= user_thresh:
                    limit = True
                    break
            cv2.rectangle(output_resized, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            cv2.putText(output_resized, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.rectangle(output_resized, (bbox_regions[user_metric][0][0]-blob, bbox_regions[user_metric][0][1]-blob), (bbox_regions[user_metric][2][0]+blob, bbox_regions[user_metric][2][1]+blob), (0, 255, 255), 2)
        cv2.imshow("Output_FINAL", output_resized)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(3)
        itr += 1
    cv2.destroyAllWindows()
    if limit:
        red_image = cv2.imread('red-color.png')
        cv2.imshow("CODE RED", red_image)
        cv2.waitKey(0)
        time.sleep(10)
    vid.release()

def main():
    user_metric, user_thresh = get_user_inputs()
    process_video(user_metric, user_thresh)

if __name__ == "__main__":
    main()
