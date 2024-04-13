import json
import time
import cv2
import easyocr
import pandas as pd
from create import create_text_file
from plotting import plot_line_graph
import datetime
from datetime import datetime
import re
from pymongo import MongoClient
from db import db_data


vid = cv2.VideoCapture(0)
reader = easyocr.Reader(['en'], gpu=True)
client = MongoClient('mongodb+srv://xabcd9172:xabcd9172@cluster0.euudrlp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


interval = 2
itr = 0
RR_RESULT = [20]
PEEP_RESULT = [15]
PIP_RESULT = [98]
FiO2_RESULT = [80]
SP_RESULT = [30]
VTe_RESULT = [102]
Tinsp_RESULT = [13]
RR_final = [15]
VTe_final = [102]
PEEP_final = [15]
PIP_final = [98]
FiO2_final = [80]
SP_final = [130]
Tinsp_final=[13]
time1 = [0]


rr_arr = []
vte_arr = []
pip_arr = []
peep_arr = []
fio2_arr = []
sp_arr = []
tinsp_arr=[]
timestamp = []

def remove_non_numeric(input_string):
    # Use regular expression to remove non-numeric characters
    return re.sub(r'[^0-9]', '', input_string)

def RR(bbox, text, blob):
    x_min, y_min = [int(val) for val in bbox[0]]
    x_max, y_max = [int(val) for val in bbox[2]]
    region=[[582, 92], [624, 92], [624, 124], [582, 124]]
    if (x_min in range(region[0][0] - blob, region[0][0] + blob) and
            x_max in range(region[2][0] - blob, region[2][0] + blob) and
            y_min in range(region[0][1] - blob, region[0][1] + blob) and
            y_max in range(region[2][1] - blob, region[2][1] + blob)):
        RR_RESULT[0] = int(remove_non_numeric(text))

def VTe(bbox, text, blob):
    x_min, y_min = [int(val) for val in bbox[0]]
    x_max, y_max = [int(val) for val in bbox[2]]
    region2 = [[556, 242], [610, 242], [610, 270], [556, 270]]
    if (x_min in range(region2[0][0] - blob, region2[0][0] + blob) and
            x_max in range(region2[2][0] - blob, region2[2][0] + blob) and
            y_min in range(region2[0][1] - blob, region2[0][1] + blob) and
            y_max in range(region2[2][1] - blob, region2[2][1] + blob)):
        VTe_RESULT[0] = int(remove_non_numeric(text))

def PEEP(bbox, text, blob):
    x_min, y_min = [int(val) for val in bbox[0]]
    x_max, y_max = [int(val) for val in bbox[2]]
    region3 = [[576, 144], [600, 144], [600, 172], [576, 172]]
    if (x_min in range(region3[0][0] - blob, region3[0][0] + blob) and
            x_max in range(region3[2][0] - blob, region3[2][0] + blob) and
            y_min in range(region3[0][1] - blob, region3[0][1] + blob) and
            y_max in range(region3[2][1] - blob, region3[2][1] + blob)):
        PEEP_RESULT[0] = int(remove_non_numeric(text))

def PIP(bbox, text, blob):
    x_min, y_min = [int(val) for val in bbox[0]]
    x_max, y_max = [int(val) for val in bbox[2]]
    region4 = [[576, 192], [618, 192], [618, 224], [576, 224]]
    if (x_min in range(region4[0][0] - blob, region4[0][0] + blob) and
            x_max in range(region4[2][0] - blob, region4[2][0] + blob) and
            y_min in range(region4[0][1] - blob, region4[0][1] + blob) and
            y_max in range(region4[2][1] - blob, region4[2][1] + blob)):
        PIP_RESULT[0] = int(remove_non_numeric(text))

def FiO2(bbox, text, blob):
    x_min, y_min = [int(val) for val in bbox[0]]
    x_max, y_max = [int(val) for val in bbox[2]]
    region5 = [[564, 290], [604, 290], [604, 318], [564, 318]]
    if (x_min in range(region5[0][0] - blob, region5[0][0] + blob) and
            x_max in range(region5[2][0] - blob, region5[2][0] + blob) and
            y_min in range(region5[0][1] - blob, region5[0][1] + blob) and
            y_max in range(region5[2][1] - blob, region5[2][1] + blob)):
        FiO2_RESULT[0] = int(remove_non_numeric(text))

def SP(bbox, text, blob):
    x_min, y_min = [int(val) for val in bbox[0]]
    x_max, y_max = [int(val) for val in bbox[2]]
    region6 = [[360, 332], [400, 332], [400, 362], [360, 362]]
    if (x_min in range(region6[0][0] - blob, region6[0][0] + blob) and
            x_max in range(region6[2][0] - blob, region6[2][0] + blob) and
            y_min in range(region6[0][1] - blob, region6[0][1] + blob) and
            y_max in range(region6[2][1] - blob, region6[2][1] + blob)):
        SP_RESULT[0] = int(remove_non_numeric(text))

def Tinsp(bbox, text, blob):
    x_min, y_min = [int(val) for val in bbox[0]]
    x_max, y_max = [int(val) for val in bbox[2]]
    region7 = [[86, 342], [126, 342], [126, 372], [86, 372]]
    if (x_min in range(region7[0][0] - blob, region7[0][0] + blob) and
            x_max in range(region7[2][0] - blob, region7[2][0] + blob) and
            y_min in range(region7[0][1] - blob, region7[0][1] + blob) and
            y_max in range(region7[2][1] - blob, region7[2][1] + blob)):
        Tinsp_RESULT[0] = int(remove_non_numeric(text))

limit = False
user_metric = input("Enter the metric you wish to keep track of: ")
user_thresh = int(input("Enter the THRESHOLD for which you ought to be alerted: "))
blob = 10
bbox_regions = {
    "VTe": [[562, 238], [616, 238], [616, 272], [562, 272]],
    "RR": [[581, 81], [625, 81], [625, 120], [581, 120]],
    "PEEP": [[582, 136], [620, 136], [620, 168], [582, 168]],
    "PIP": [[582, 188], [624, 188], [624, 218], [582, 218]],
    "FiO2": [[30, 324], [70, 324], [70, 354], [30, 354]],
    "SP": [[360, 332], [400, 332], [400, 362], [360, 362]],
    'Tinsp': [[86, 342], [126, 342], [126, 372], [86, 372]]
}
while not limit:
    ret, frame = vid.read()
    output_resized = frame
    results = reader.readtext(output_resized)
    res_df = pd.DataFrame(results, columns=['bbox', 'text', 'conf'])
    filtered_df = res_df[res_df['conf'] >= 0.55]
    filtered_results = [item for item in results if item[2] >= 0.55]
    value_stream = []
    for detection in filtered_results:
        bbox = detection[0]
        text = detection[1]
        value_stream.append(text)
        x_min, y_min = [int(val) for val in bbox[0]]
        x_max, y_max = [int(val) for val in bbox[2]]
        RR(bbox, text, blob)
        VTe(bbox, text, blob)
        PEEP(bbox, text, blob)
        PIP(bbox, text, blob)
        FiO2(bbox, text, blob)
        SP(bbox, text, blob)
        Tinsp(bbox, text, blob)
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
    if itr%20 == 0:
        print(filtered_df)
        rr_arr.append(RR_RESULT[0])
        vte_arr.append(VTe_RESULT[0])
        sp_arr.append(SP_RESULT[0])
        fio2_arr.append(FiO2_RESULT[0])
        pip_arr.append(PIP_RESULT[0])
        peep_arr.append(PEEP_RESULT[0])
        tinsp_arr.append(Tinsp_RESULT[0])
        timestamp.append(itr)
        #print(rr_arr)
        json_data = {
            "RR": rr_arr,
            "Vte": vte_arr,
            "SP": sp_arr,
            "FiO2": fio2_arr,
            "PIP": pip_arr,
            "PEEP": peep_arr,
            'Tinsp': tinsp_arr,
            "timestamp": timestamp
        }
        with open("json.txt", "w") as file:
            json.dump(json_data, file)
        create_text_file("RR.txt", RR_RESULT[0])
        create_text_file("VTe.txt", VTe_RESULT[0])
        create_text_file("PEEP.txt", PEEP_RESULT[0])
        create_text_file("PIP.txt", PIP_RESULT[0])
        create_text_file("FiO2.txt", FiO2_RESULT[0])
        create_text_file("SP.txt", SP_RESULT[0])
        create_text_file('Tinsp.txt', Tinsp_RESULT[0])
        RR_final.append(RR_RESULT[0])
        VTe_final.append(VTe_RESULT[0])
        PEEP_final.append(PEEP_RESULT[0])
        PIP_final.append(PIP_RESULT[0])
        FiO2_final.append(FiO2_RESULT[0])
        SP_final.append(SP_RESULT[0])
        Tinsp_final.append(Tinsp_RESULT[0])
        time1.append(itr)

        db_data(RR_RESULT[0], VTe_RESULT[0], PEEP_RESULT[0], PIP_RESULT[0], FiO2_RESULT[0], SP_RESULT[0], Tinsp_RESULT[0])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    itr += 1
cv2.destroyAllWindows()

if limit:
    cv2.imwrite('threshold.png', output_resized)
    cv2.waitKey(0)
    time.sleep(10)
    client.close()

vid.release()
cv2.destroyAllWindows()
