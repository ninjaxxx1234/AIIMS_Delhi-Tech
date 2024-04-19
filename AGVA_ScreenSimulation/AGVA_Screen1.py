import cv2
import time
import random


fi02 = str(random.randint(21, 32))
Tinsp = ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '2.0']
rr = [str(i) for i in range(20, 31)]
trigg_flow = ['5.0', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '6.0']
PEEP = [str(i) for i in range(2, 13)]
supp_press = [str(i) for i in range(3, 14)]
slope = [str(i) for i in range(10, 21)]
pinsp = [str(i) for i in range(18, 29)]


sp_arr = [
    12, 9, 14, 14, 13, 11, 11, 12, 6, 5, 8, 11, 6, 5, 13, 12, 14, 8, 8, 14, 9, 5, 13, 5, 13, 14, 12, 5, 14, 10,
    5, 6, 14, 11, 10, 14, 10, 13, 6, 8, 12, 10, 9, 10, 9, 8, 11, 13, 11, 7, 13, 9, 14, 10, 11, 10, 5, 14, 14, 10,
    9, 10, 9, 6, 11, 9, 10, 8, 6, 11, 13, 8, 7, 8, 11, 6, 13, 6, 8, 11, 6, 5, 13, 11, 5, 6, 11, 14, 11, 5, 5, 10,
    6, 12, 8, 14, 11, 5, 5, 9
]

vte_arr = [
    129, 114, 115, 149, 129, 112, 125, 150, 142, 126, 130, 146, 126, 107, 126, 117, 122, 126, 130, 117, 149,
    114, 148, 138, 137, 126, 143, 140, 127, 132, 116, 110, 133, 135, 114, 127, 135, 123, 147, 131, 110, 145,
    116, 138, 108, 121, 138, 116, 116, 125, 135, 111, 115, 150, 106, 106, 129, 121, 125, 129, 120, 143, 124,
    136, 109, 119, 111, 133, 136, 120, 142, 122, 146, 148, 136, 140, 138, 130, 138, 148, 147, 132, 150, 129,
    106, 108, 143, 107, 141, 109, 124, 144, 116, 115, 149, 146, 119, 150, 143, 150
]

pip_arr = [
    19, 17, 19, 16, 22, 18, 17, 22, 17, 13, 19, 16, 14, 19, 13, 16, 17, 18, 18, 16, 15, 22, 18, 18, 22, 17, 18, 12,
    20, 12, 19, 21, 18, 12, 22, 12, 22, 18, 12, 17, 12, 13, 19, 22, 18, 13, 14, 20, 16, 19, 20, 17, 22, 12, 17, 21,
    21, 20, 17, 18, 16, 12, 22, 19, 21, 16, 14, 12, 19, 13, 20, 20, 12, 17, 15, 14, 18, 15, 18, 21, 17, 21, 16, 18,
    17, 22, 14, 12, 22, 13, 21, 13, 16, 12, 19, 22, 21, 13, 13, 13
]

peep_arr = [
    10, 9, 17, 18, 13, 5, 13, 8, 9, 11, 10, 9, 18, 15, 13, 3, 6, 15, 9, 18, 12, 17, 15, 3, 8, 4, 7, 15, 5, 18, 16,
    10, 11, 5, 7, 9, 7, 4, 9, 13, 12, 18, 8, 16, 14, 17, 14, 8, 12, 9, 3, 11, 15, 3, 8, 8, 3, 17, 8, 7, 7, 12, 16,
    12, 8, 13, 15, 4, 15, 7, 4, 3, 3, 4, 12, 11, 18, 10, 14, 13, 12, 18, 17, 4, 3, 6, 9, 14, 5, 6, 16, 9, 12, 6, 18,
    11, 12, 14, 3, 7
]

fio2_arr = [
    24, 27, 29, 32, 31, 21, 32, 31, 18, 37, 25, 31, 20, 23, 34, 31, 29, 19, 25, 20, 19, 18, 32, 22, 22, 34, 30, 31,
    30, 36, 35, 33, 37, 25, 21, 32, 32, 37, 20, 30, 32, 19, 38, 27, 37, 27, 18, 21, 24, 21, 27, 26, 37, 31, 23, 38,
    37, 27, 25, 22, 27, 36, 29, 34, 36, 23, 22, 27, 30, 18, 33, 26, 33, 18, 36, 37, 27, 24, 22, 31, 33, 35, 20, 33,
    37, 38, 22, 18, 22, 21, 35, 32, 24, 36, 38, 35, 38, 24, 21, 21
]

rr_arr = [
    16, 21, 31, 24, 22, 30, 16, 26, 23, 15, 20, 16, 31, 29, 25, 15, 21, 26, 19, 25, 34, 31, 22, 30, 22, 17, 22, 27,
    19, 34, 21, 34, 16, 30, 31, 21, 25, 16, 15, 27, 15, 24, 32, 32, 17, 24, 17, 23, 23, 25, 33, 31, 15, 29, 19, 15,
    20, 20, 16, 33, 24, 29, 27, 29, 16, 25, 31, 33, 28, 20, 18, 28, 17, 24, 31, 20, 18, 15, 22, 26, 23, 27, 33, 19,
    21, 27, 26, 27, 27, 19, 26, 34, 27, 28, 15, 35, 26, 33, 17, 15
]

hr_arr = [
    5.1, 5.2, 5.6, 6.3, 5.2, 5.8, 5.3, 4.7, 5.5, 6.1, 5.1, 6.2, 6.3, 6.1, 5.1, 4.9, 5.0, 5.3, 5.0, 4.8, 5.5, 4.9, 4.9,
    6.4, 5.4, 5.1, 5.8, 5.1, 6.0, 6.3, 5.6, 5.6, 6.0, 5.6, 4.9, 5.2, 6.4, 5.1, 5.5, 5.4, 5.0, 5.7, 5.7, 5.3, 5.9, 6.1,
    5.4, 5.2, 6.0, 6.1, 5.8, 5.8, 5.1, 5.0, 4.8, 5.9, 6.2, 6.2, 5.2, 5.0, 5.0, 5.1, 5.4, 6.3, 5.1, 4.7, 5.1, 6.0, 6.2,
    5.7, 6.0, 6.4, 4.8, 5.7, 5.2, 5.1, 5.1, 5.2, 5.8, 5.6, 6.3, 5.8, 5.4, 5.7, 5.9, 5.6, 5.7, 6.0, 6.2, 6.3, 5.5, 6.0,
    5.4, 5.5, 5.3, 4.9, 5.1, 4.8, 6.2, 5.2
]

tinsp_arr = [
    2.1, 2.1, 3.4, 2.7, 2.2, 2.8, 3.4, 3.0, 1.3, 1.1, 1.0, 1.3, 2.2, 2.7, 1.3, 2.7, 2.0, 1.1, 3.1, 2.7, 1.7, 2.6,
    3.1, 3.1, 1.8, 3.2, 2.8, 2.4, 1.9, 3.2, 2.3, 2.3, 1.1, 3.0, 2.2, 2.2, 2.0, 3.1, 1.7, 1.4, 1.6, 2.2, 2.2, 2.5, 1.9,
    1.2, 1.3, 1.6, 2.0, 2.2, 1.2, 1.9, 1.8, 2.1, 1.5, 3.3, 3.1, 1.6, 2.3, 2.0, 3.4, 1.2, 1.7, 2.1, 2.3, 2.7, 1.2, 2.7,
    3.4, 1.7, 1.4, 2.5, 1.4, 2.5, 3.0, 2.5, 2.1, 1.2, 1.3, 2.9, 2.0, 2.5, 1.4, 3.5, 2.2, 1.3, 3.5, 2.1, 1.0, 3.4, 2.6,
    3.1, 1.2, 1.6, 2.8, 2.4, 1.9, 2.7, 1.4, 2.9
]

sp_arr2 = []
rr_arr2 = []
fio2_arr2 = []
vte_arr2 = []
pip_arr2 = []
peep_arr2 = []
hr_arr2 = []
tinsp_arr2 = []



resp_rate = [str(i) for i in range(20, 31)]
peep = [str(i) for i in range(2, 13)]
pip = [str(i) for i in range(19, 30)]
vte = [str(i) for i in range(140, 151)]
FIO2 = [str(i) for i in range(21, 32)]
spo2 = [str(i) for i in range(98, 109)]
hr = [str(i) for i in range(83, 94)]
padding = 7
pl1 = -7
path = 'blank3.0.png'
image = cv2.imread(path)
image = cv2.resize(image, (1600, 850))
positions = [
    (166, 723+padding),
    (300+pl1, 722+padding),
    (475, 725+padding),
    (605+pl1, 726+padding),
    (784, 723+padding),
    (940, 725+padding),
    (1082, 725+padding),
    (1240, 722+padding),
    (1400, 173),
    (1400, 288),
    (1407, 402),
    (1368, 520),
    (1400, 635),
    (1423, 68),
    (1294, 68)

]

# Accessing individual coordinates
position1 = positions[0]
position2 = positions[1]
position3 = positions[2]
position4 = positions[3]
position5 = positions[4]
position6 = positions[5]
position7 = positions[6]
position8 = positions[7]

position11 = positions[8]
position22 = positions[9]
position33 = positions[10]
position44 = positions[11]
position55 = positions[12]

position111 = positions[13]
position222 = positions[14]

font_scale2 = 1
thickness2 = 2
font_scale1 = 2
thickness1 = 2
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
thickness = 2
color = (255, 255, 255)


cv2.waitKey(1)
time.sleep(3)

ind = 0
while True:
    fi02 = str(random.randint(21, 32))
    Tinsp = str(round(random.uniform(1, 2), 1))
    rr = str(random.randint(20, 31))
    trigg_flow = str(round(random.uniform(5, 6), 1))
    PEEP = str(random.randint(2, 13))
    supp_press = str(random.randint(3, 14))
    slope = str(random.randint(10, 21))
    pinsp = str(random.randint(18, 29))
    spo2 = str(random.randint(98, 109))
    hr = str(random.randint(83, 94))
    vte = str(random.randint(140, 151))
    resp_rate = str(random.randint(21, 32))
    pip = str(random.randint(20, 30))

    image1 = cv2.putText(image.copy(), str(fio2_arr[ind]), position1, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, str(tinsp_arr[ind]), position2, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, str(rr_arr[ind]), position3, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, str(hr_arr[ind]), position4, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, str(peep_arr[ind]), position5, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, supp_press, position6, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, slope, position7, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, pinsp, position8, font, font_scale, color, thickness, cv2.LINE_AA)

    image1 = cv2.putText(image1, str(rr_arr[ind]), position11, font, font_scale1, color, thickness1, cv2.LINE_AA)
    image1 = cv2.putText(image1, str(peep_arr[ind]), position22, font, font_scale1, color, thickness1, cv2.LINE_AA)
    image1 = cv2.putText(image1, str(pip_arr[ind]), position33, font, font_scale1, color, thickness1, cv2.LINE_AA)
    image1 = cv2.putText(image1, str(vte_arr[ind]), position44, font, font_scale1, color, thickness1, cv2.LINE_AA)
    image1 = cv2.putText(image1, str(fio2_arr[ind]), position55, font, font_scale1, color, thickness1, cv2.LINE_AA)

    image1 = cv2.putText(image1, spo2, position111, font, font_scale2, color, thickness2, cv2.LINE_AA)
    image1 = cv2.putText(image1, hr, position222, font, font_scale2, color, thickness2, cv2.LINE_AA)

    cv2.imshow("Image", image1)
    cv2.waitKey(1)
    ind += 1

    time.sleep(7)

cv2.waitKey(0)
cv2.destroyAllWindows()
