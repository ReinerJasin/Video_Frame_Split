# Video Frame Splitter  

This Python script extracts frames from a video file at a reduced frame rate and saves them as images. It utilizes OpenCV (`cv2`) for video processing.  

## 📂 Repository Structure  

```
Video_Frame_Split/  
│── video/               # Folder to place the source video  
│── output/              # Folder where extracted frames will be saved  
│── venv/                # Conda virtual environment (optional)  
│── video_frame_split.py # Main script for frame extraction  
│── README.md            # Documentation  
```

## 🔧 Requirements  

- Python 3.x  
- OpenCV (`cv2`)  
- Conda (optional, for virtual environment)  

## 🛠️ Setup  

### 1️⃣ Clone the Repository  

```
git clone https://github.com/ReinerJasin/Video_Frame_Split.git  
cd Video_Frame_Split  
```

### 2️⃣ Setup Environment  

#### **Using Conda (Recommended)**  

If you're using Conda, activate the existing environment:  

```
conda activate ./venv  
```

If you need to create a new Conda environment, run:  

```
conda create --prefix ./venv python=3.9 -y  
conda activate ./venv  
pip install -r requirements.txt  # If you have a requirements.txt file  
```

#### **Without Conda**  

If not using Conda, install OpenCV manually:  

```
pip install opencv-python  
```

## ▶️ Usage  

1. **Place Your Video**  
   - Copy your video file into the `video/` folder.  
   - Update the script (`video_frame_split.py`) to match your video file name.  

2. **Run the Script**  

```
python video_frame_split.py  
```

3. **Output**  
   - Extracted frames will be saved in the `output/` folder as `frame_<index>.jpg`.  
