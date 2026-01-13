❤️ Heart Disease Prediction System

A web-based machine learning application built using Django and Python that predicts whether a patient is likely to have heart disease based on medical attributes.

This project integrates:

A trained KNN machine learning model

A Django web interface

A real medical dataset

📌 Project Objective

To help detect the risk of heart disease by analyzing patient health data such as:

Age

Blood pressure

Cholesterol

Heart rate

Chest pain type

And more

The system predicts whether the patient is Normal or At Risk.

🧠 Machine Learning Model

The ML model is trained using the K-Nearest Neighbors (KNN) algorithm on a heart disease dataset (heart.csv).
The trained model is stored as:

pipeline.pkl


It is loaded by the Django backend to generate real-time predictions.

🗂 Project Structure
heart_d_p/
│
├── heart_d_p/          → Django project settings
├── users/             → Django app (auth + prediction logic)
├── templates/         → HTML pages
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   └── success pages
│
├── data.ipynb         → Data analysis & preprocessing
├── notebook.ipynb    → Model training
├── pipeline.pkl      → Trained ML model
├── heart.csv         → Dataset
├── db.sqlite3        → Django database
├── manage.py         → Django entry file
└── README.md

🖥 Features

✔ User registration & login
✔ Patient health data input
✔ Machine learning prediction
✔ Real-time disease detection
✔ Data stored in database
✔ Clean Django UI

⚙ Technologies Used
Technology	Purpose
Python	Core programming
Django	Web framework
Pandas	Data handling
NumPy	Computations
Scikit-Learn	Machine learning
HTML / CSS	Frontend
SQLite	Database
▶ How to Run the Project
1️⃣ Install dependencies
pip install django pandas numpy scikit-learn

2️⃣ Run the Django server
python manage.py runserver

3️⃣ Open in browser
http://127.0.0.1:8000

📊 Dataset

The dataset heart.csv contains medical attributes such as:

Age

Sex

Chest pain

Cholesterol

Blood pressure

ECG results

Heart rate

📈 Output

After entering patient details, the system predicts:

Heart Disease Detected
or

No Heart Disease

The result is shown instantly on the web interface.

👤 Author

Yateen R
B.Tech Computer Science Engineering
GitHub: https://github.com/yateen-r

LinkedIn: https://www.linkedin.com/in/YateenR/

⭐ If you like this project, give it a star!
