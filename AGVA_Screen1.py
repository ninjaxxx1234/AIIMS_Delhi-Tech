import cv2
import time

fi02 = ['21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
Tinsp = ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8', '2.0']
rr = ['20', '21', '22', '23', '24', '25', '26', '27', '28', '30']
trigg_flow = ['5.0', '5.1', '5.2', '5.3', '5.4', '5.5', '5.6', '5.7', '5.8', '6.0']
PEEP = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '12']
supp_press = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '13']
slope = [str(i) for i in range(10, 21)]
pinsp = ['18', '19', '20', '21', '22', '23', '24', '25', '26', '28']

resp_rate = [str(i) for i in range(20, 31)]
peep = [str(i) for i in range(2, 13)]
pip = [str(i) for i in range(19, 30)]
vte = [str(i) for i in range(140, 151)]
FIO2 = [str(i) for i in range(21, 32)]
spo2 = [str(i) for i in range(98, 109)]
hr = [str(i) for i in range(83, 94)]

path = 'blank.png'
image = cv2.imread(path)
image = cv2.resize(image, (1600, 850))
positions = [
    (166, 723),
    (319, 722),
    (475, 725),
    (625, 726),
    (784, 723),
    (940, 725),
    (1082, 725),
    (1240, 722),
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

font_scale2 = 0.75
thickness2 = 2
font_scale1 = 2
thickness1 = 2
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 1
color = (255, 255, 255)


cv2.waitKey(1)
time.sleep(3)  # Initial delay

for f in range(10):
    image1 = cv2.putText(image.copy(), fi02[f], position1, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, Tinsp[f], position2, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, rr[f], position3, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, trigg_flow[f], position4, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, PEEP[f], position5, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, supp_press[f], position6, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, slope[f], position7, font, font_scale, color, thickness, cv2.LINE_AA)
    image1 = cv2.putText(image1, pinsp[f], position8, font, font_scale, color, thickness, cv2.LINE_AA)

    image1 = cv2.putText(image1, resp_rate[f], position11, font, font_scale1, color, thickness1, cv2.LINE_AA)
    image1 = cv2.putText(image1, peep[f], position22, font, font_scale1, color, thickness1, cv2.LINE_AA)
    image1 = cv2.putText(image1, pip[f], position33, font, font_scale1, color, thickness1, cv2.LINE_AA)
    image1 = cv2.putText(image1, vte[f], position44, font, font_scale1, color, thickness1, cv2.LINE_AA)
    image1 = cv2.putText(image1, FIO2[f], position55, font, font_scale1, color, thickness1, cv2.LINE_AA)

    image1 = cv2.putText(image1, spo2[f], position111, font, font_scale2, color, thickness2, cv2.LINE_AA)
    image1 = cv2.putText(image1, hr[f], position222, font, font_scale2, color, thickness2, cv2.LINE_AA)

    cv2.imshow("Image", image1)
    cv2.waitKey(1)
    time.sleep(1)

cv2.waitKey(0)
cv2.destroyAllWindows()
