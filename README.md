# Joint Detection System

## 📌 Introduction
This project is a **Machine Learning model** built using **Python** to detect whether a human joint is **Normal** or **Abnormal** based on:
- Knee Angle
- Hip Angle
- Movement Range

The dataset is manually created and stored directly in the code.  
The model is trained using the **Random Forest Classifier** from **scikit-learn**.

---

## ⚙️ How It Works
1. A dataset is created with joint measurements and corresponding labels:
   - `0` → Normal Joint
   - `1` → Abnormal Joint
2. Data is split into **training** and **testing** sets using `train_test_split`.
3. A **Random Forest Classifier** is trained on the training set.
4. The model predicts the label for:
   - Test dataset (to check accuracy)
   - New data input (to detect joint condition)

---

## 📂 Dataset Example
| knee_angle | hip_angle | movement | label |
|------------|-----------|----------|-------|
| 160        | 130       | 45       | 0     |
| 150        | 120       | 50       | 0     |
| 170        | 135       | 60       | 0     |
| 120        | 100       | 30       | 1     |
| 110        | 90        | 20       | 1     |
| 140        | 115       | 35       | 1     |
| 125        | 105       | 25       | 1     |

---

## 📜 Requirements
Make sure you have the following installed:
```bash
pip install pandas scikit-learn
```

---

## ▶️ How to Run
1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/joint-detection-system.git
   ```
2. **Navigate to the project folder**
   ```bash
   cd joint-detection-system
   ```
3. **Run the script**
   ```bash
   python main.py
   ```

---

## 📊 Output Example
```
Data      knee_angle  hip_angle  movement  label
0         160        130        45.0      0
...
Model training complete.
Accuracy: 1.0
New data for prediction: [[155, 125, 47.5]]
Joint is Normal
```

---

## 📌 Notes
- You can adjust the dataset to include more samples for better accuracy.
- Modify `new_data` in the script to test different joint measurements.
- The dataset currently uses small values for demonstration purposes only.

---

## 🏷️ License
This project is licensed under the **MIT License** – feel free to use, modify, and share.
