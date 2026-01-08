# oil-tank-detection
YOLOv5 project for detecting oil storage tanks


Create run all script at the end


# Oil Tank Detection

## Setup

1. Clone the repo
```bash
git clone https://github.com/yourusername/oil-tank-detection.git
cd oil-tank-detection


#Install requirements
pip install -r requirements.txt

#Download dataset
python scripts/download_data.py

Download https://pytorch.org/get-started/locally/ 

# Clone YOLOv5 (outside your repo)
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt


for running model python yolov5/train.py --img 512 --batch 16 --epochs 50 --data oil_tanks.yaml --weights yolov5s.pt --project runs/train --name oil_tank_experiment
