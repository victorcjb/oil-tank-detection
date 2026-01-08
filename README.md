# oil-tank-detection
- Can easily swap datasets, retrain models, or adjust thresholds

Goal: Project trains and runs a YOLOv5 model to detect oil tanks in images. Can easily swap data sets, retrain models, or adjust thresholds. I utilized the Yolov5s model. Cleaned up data, formatted into Yolo format, split into train and test groups, and fine-tuned the model.

Input: Areial/satellite image data from Kaggle
Output: Model builds bounding boxes around detected oil tanks 


- Still in process of fine tunning this model. I ran it with 50 epochs. Holes in accuracy, that will want to improve upon.
- Future improvements include improving accurage and more diverse training data (also need more computing power)


# Setup

1. Clone the repo
```bash
git clone https://github.com/yourusername/oil-tank-detection.git
cd oil-tank-detection

#Install requirements
pip install -r requirements.txt

#Download dataset
python scripts/download_data.py
python config.py
python convert_to_yolo_format.py


#Make sure to download pytorch correctly
Download https://pytorch.org/get-started/locally/ 

# Clone YOLOv5 (outside your repo)
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt

#Run Yolov5 model
for running model python yolov5/train.py --img 512 --batch 16 --epochs 50 --data oil_tanks.yaml --weights yolov5s.pt --project runs/train --name oil_tank_experiment
