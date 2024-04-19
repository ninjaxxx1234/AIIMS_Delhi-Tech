import cv2
from rembg import remove
from matplotlib import pyplot as plt
import easyocr
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math


path = 'input_vid2_hd.mp4'
cap = cv2.VideoCapture(path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total Frames:", total_frames)
reader = easyocr.Reader(['en'], gpu=True)
sorter = 0.55
def find_nearest_coordinate(start_coord, remaining_coords):
    min_distance = float('inf')
    nearest_coord = None
    for coord in remaining_coords:
        distance = math.sqrt((start_coord[0] - coord[0])**2 + (start_coord[1] - coord[1])**2)
        if distance < min_distance:
            min_distance = distance
            nearest_coord = coord
    return nearest_coord

def sort_coordinates_by_nearest(start_coord, coordinates, sorted_data):
    sorted_coordinates = [start_coord]
    sorted_results = []
    remaining_coords = coordinates.copy()
    remaining_data = sorted_data.copy()
    remaining_coords.remove(start_coord)
    nearest_index = coordinates.index(start_coord)
    sorted_results.append(sorted_data[nearest_index][1])

    while remaining_coords:
        nearest_coord = find_nearest_coordinate(sorted_coordinates[-1], remaining_coords)
        nearest_index = coordinates.index(nearest_coord)
        sorted_coordinates.append(nearest_coord)
        sorted_results.append(sorted_data[nearest_index][1])
        remaining_coords.remove(nearest_coord)

    return sorted_coordinates, sorted_results
key_coords = [[[0.7947598253275109, 0.2577092511013216], 'Respiratory Rate'], [[0.7941359950093575, 0.3623348017621145], 'PEEP'], [[0.7985028072364317, 0.46255506607929514], 'PIP'], [[0.7785402370555209, 0.5682819383259912], 'VTe'], [[0.7922645040548971, 0.6718061674008811], 'FiO2'], [[0.7136618839675608, 0.7687224669603524], 'PINSP'], [[0.6338116032439176, 0.7731277533039648], 'Slope'], [[0.5601996257018091, 0.775330396475771], 'Support Pressure'], [[0.48346849656893326, 0.776431718061674], 'PEEP'], [[0.4017467248908297, 0.7775330396475771], 'Trigger Flow'], [[0.3256394260761073, 0.7775330396475771], 'Respiratory Rate'], [[0.24703680598877106, 0.7775330396475771], 'Tinsp'], [[0.1671865252651279, 0.7797356828193832], 'FiO2']]
def find_nearest_key(start_coord, key_coords):
    min_distance = float('inf')
    nearest_coord = None
    nearest_key = None
    for coord in key_coords:
        distance = math.sqrt((start_coord[0] - coord[0][0])**2 + (start_coord[1] - coord[0][1])**2)
        if distance < min_distance:
            min_distance = distance
            nearest_coord = coord[0]
            nearest_key = coord[1]
    return nearest_key

def plot_sorted_data(result_data):
    fig, ax = plt.subplots(figsize=(8, 5))
    sorted_data = [item for item in result_data if item[2] >= sorter]

    ax.set_xlim(0, 2000)
    ax.set_ylim(1200, 0)

    for rect_data, label, _ in sorted_data:
        rect = patches.Polygon(rect_data, closed=True, edgecolor='r', facecolor='none')
        ax.add_patch(rect)

        center_x = (rect_data[0][0] + rect_data[2][0]) / 2
        center_y = (rect_data[0][1] + rect_data[2][1]) / 2

        ax.text(center_x, center_y, label, color='b', ha='center', va='center')

    plt.show()
frame_data = {}
for frame_idx in range(total_frames):
    token = []
    ret, frame = cap.read()
    width = frame.shape[1]
    height = frame.shape[0]
    if not ret:
        break

    # Display every 32nd frame
    if frame_idx % 32 == 0:
        bg_removed = remove(frame)

        result1 = reader.readtext(bg_removed)
        data = result1
        #plot_sorted_data(result1)
        sorted_data = [item for item in data if item[2] >= sorter]
        coordinates = [item[0][0] for item in sorted_data]  # Extracting bottom-left coordinates from sorted data
        sorted_by_nearest_coords, sorted_by_nearest_results = sort_coordinates_by_nearest(coordinates[0], coordinates, sorted_data)

        for coord, result in zip(sorted_by_nearest_coords, sorted_by_nearest_results):
            rel_width, rel_height = coord[0]/width, coord[1]/height
            #print(f"Coordinate: {rel_width, rel_height}, Result: {result}")
            token.append([[rel_width, rel_height], result])
        frame_data[frame_idx] = token

        #plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        #plt.show()
video_results = []

# Assuming frame_data is a dictionary
for frame, frame_values in frame_data.items():
    frame_results = {}
    for data in frame_values:
        coord = data[0]
        value = data[1]
        key_for_val = find_nearest_key(coord, key_coords)
        # Check if the value is numeric before assigning
        if value.isdigit():
          frame_results[key_for_val] = value
    video_results.append(frame_results)
print(frame_data)
print(video_results)
# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
