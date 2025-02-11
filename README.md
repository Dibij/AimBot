# **Aimbot Using OpenCV & YOLOv3**  
An **experimental** aimbot that detects enemies using **YOLOv3** and **OpenCV** to automatically aim in **Free Fire** (or other FPS games).  

---

## ⚠ **Disclaimers**  
### 🚨 **For Educational Purposes Only**  
> **This project is purely for educational and research purposes.**  
> I do **NOT** support, encourage, or promote cheating in online games.  
> Using this script in **multiplayer games** may result in **account bans** or **legal consequences.**  
> **Use at your own risk. The author is NOT responsible for misuse.**  

### ⚠ **Not Perfect – Still in Progress**  
> This **aimbot is not flawless** – it's still a **work in progress**.  
> It **lags**, is **inconsistent**, and may not always work as expected.  
> Expect **bugs**, **slow FPS**, and **imperfections** in detection and aiming.  
> **Do NOT expect a fully polished cheat – this is just an experiment.**  

---

## **🎥 Inspiration**
This project was inspired by **Chessy AI** on YouTube, who creates **AI-based aimbots and automation scripts**.  
Check out their channel for more cool AI automation content! 🎯  

---

## **🔧 Features**
✔ **AI-powered enemy detection** using YOLOv3  
✔ **Auto-aim and headshot feature**  
✔ **Toggle On/Off** with the "H" key  
✔ **Optimized for performance (but may experience FPS drops depending on hardware)**  
✔ **No need for manual aiming once enabled**  

---

## **📜 How It Works**
- Press **"H"** → **Aimbot starts** and automatically aims/shoots  
- Press **"H" again** → **Aimbot stops**  
- The script captures the game screen and detects enemies  
- Moves the **mouse cursor to the enemy's head** for an accurate shot  

---

## **📂 Installation**
### **1️⃣ Requirements**
- **Python 3.8+**
- **pip** (Python Package Manager)

### **2️⃣ Install Dependencies**
```bash
pip install numpy pyautogui opencv-python opencv-contrib-python pywin32
```

### **3️⃣ Download YOLOv3 Files**
Place the following files inside the **"Aimbot"** folder:
- [`yolov3.cfg`](https://github.com/pjreddie/darknet/blob/master/cfg/yolov3.cfg) (YOLOv3 configuration file)
- [`yolov3.weights`](https://pjreddie.com/media/files/yolov3.weights) (YOLOv3 pre-trained weights)

---

## **🚀 Usage**
### **Run the script:**
```bash
python main.py
```
### **Controls:**
- **Press "H"** → Toggle Aimbot ON/OFF
- **Press "Esc"** → Exit the program

---

## **📜 Legal Note**
🚨 **Using this in online multiplayer games may result in bans!**  
🔴 **This script is intended for educational use only.**  
🔴 **The author is NOT responsible for misuse or any consequences.**  
🔴 **Do not use this for cheating in online games!**  

---

🔹 **This is a buggy, laggy, and imperfect experiment – use responsibly & for learning purposes only!**  
```
