#Convert labels_coco.json to format
import sys
import os
import json
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split
import numpy as np 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import get_data_path
from tqdm import tqdm

#Define image size and folder of downloaded data pulled from download_data.py
Image_size = 512
Path = Path
Original_images_folder = os.path.join(get_data_path(), "Oil Tanks/image_patches")



#Organize data into YOLO folder format
Output_folder = "Yolo_Dataset"
Image_train = os.path.join(Output_folder, "images/train")
Image_test = os.path.join(Output_folder, "images/test")
Label_train = os.path.join(Output_folder, "labels/train")
Label_test = os.path.join(Output_folder, "labels/test")

#Tank labels predefined
label_number = {
    "Tank": 0,
    "Tank Cluster": 1,
    "Floating Head Tank": 2
}

#From labels_coco.json format (Kaggle dataset)
def bbox_conversion(box_dict):
    x_array = np.array([p["x"] for p in box_dict])
    y_array = np.array([p["y"]for p in box_dict])

    xmin = x_array.min()
    ymin = y_array.min()
    xmax = x_array.max()
    ymax = y_array.max()

    width = xmax - xmin
    height = ymax - ymin

    x_center = (xmin + width / 2) / Image_size
    y_center = (ymin + height / 2) / Image_size
    w_standard = x_center / Image_size
    h_standard = y_center / Image_size

    #Return in YOLO format
    return x_center, y_center, w_standard, h_standard


#Main Function
def main():
    for d in [Image_train, Image_test, Label_train, Label_test]:
        os.makedirs(d, exist_ok=True)
    
    labels_path = os.path.join(get_data_path(), "Oil Tanks/labels.json")
    json_labels = json.load(open(labels_path))

    large_image_ids = sorted(list(set([entry['file_name'].split('_')[0] 
        for entry in json_labels if entry['label'] != 'Skip'])))
    
    all_files = [entry["file_name"] for entry in json_labels if not (isinstance(entry["label"], str) and entry["label"].lower() == "skip")]
    train_files, test_files = train_test_split(all_files, test_size=0.2, random_state=42)

    for entry in tqdm(json_labels):
        filename = entry["file_name"]  
        if filename in train_files:
            Image_dst = Image_train
            Label_dst = Label_train
        elif filename in test_files:
            Image_dst = Image_test
            Label_dst = Label_test
        else:
            print(f"Skipping {filename}, not in train or test split")
            continue

        source_image = os.path.join(Original_images_folder, filename)
        destination_image = os.path.join(Image_dst, filename)
        shutil.copy(source_image, destination_image)

        label_file = os.path.join(Label_dst, filename.replace(".jpg",".txt"))


        with open(label_file, "w") as f:
            for label_name in entry["label"]:
                if label_name not in label_number:
                    print(f"Skipping unknown label '{label_name}' in {filename}")
                    continue

                class_id = label_number[label_name]
                for box in entry["label"][label_name]:
                    x, y, w, h = bbox_conversion(box["geometry"])
                    f.write(f"{class_id} {x} {y} {w} {h}\n")

    print("YOLO dataset created with success.")

if __name__ == "__main__":
    main()


print("Number of train images:", len(os.listdir(Image_train)))
print("Number of test images:", len(os.listdir(Image_test)))
