# 🌱 GoAgro - Crop Recommendation System

GoAgro is a **Machine Learning and Flask-based web application** that recommends the most suitable crop for cultivation based on soil nutrients (N, P, K), weather parameters (temperature, humidity, rainfall), and soil pH.  

This project helps farmers and agricultural enthusiasts make data-driven decisions for better productivity.  

---

## ✨ Features

* **User-Friendly Interface:** A clean and simple web form for data input.
* **Instant Predictions:** Get real-time crop recommendations without any delay.
* **Data-Driven:** The model is trained on a comprehensive agricultural dataset to ensure accuracy.
* **Scalable Architecture:** Built with Flask, the application is lightweight and can be easily deployed.

---

## 💻 Tech Stack

* **Backend:** Flask
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Frontend:** HTML, CSS (within the `templates` and `static` directories)
* **Model Deployment:** Joblib

---

## 📂 Project Structure

The project follows a standard Flask web application structure, separating the machine learning model, web logic, and frontend templates.

```
GoAgro/
├── static/                 # CSS, JS, and image files
├── templates/
│   └── home.html           # Main HTML page for user input and results
├── Crop_recommendation.csv # Dataset used for training the model
├── app.py                  # Core Flask application logic
├── model.ipynb             # (Optional) Jupyter Notebook for model training
├── model.joblib            # The trained Random Forest classification model
├── scaler.joblib           # The saved data scaler
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.8 or higher
* pip package manager

### Installation and Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/GoAgro.git](https://github.com/your-username/GoAgro.git)
    cd GoAgro
    ```
    *(Replace `your-username` with your actual GitHub username)*

2.  **Create and activate a virtual environment:**
    Using a virtual environment is highly recommended to keep project dependencies isolated.
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    The `requirements.txt` file contains all the necessary Python packages.
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Start the Flask server:**
    Run the `app.py` script from the root directory of the project.
    ```sh
    python app.py
    ```

2.  **Access the application in your browser:**
    Open your web browser and go to the following URL:
    ```
    [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```
    You will see the GoAgro home page.

---

## 🔧 How It Works

The application operates in a simple, sequential flow:

1.  **User Input:** A user enters the seven required environmental and soil parameters into the web form on `home.html`.
2.  **Data Submission:** The form submits this data to the `/predict` route in the `app.py` script via a POST request.
3.  **Data Preprocessing:** The Flask backend receives the data, converts it into a NumPy array, and uses the pre-fitted `scaler.joblib` to scale the features. This is a critical step, as the model was trained on scaled data.
4.  **Prediction:** The scaled data is then passed to the trained `model.joblib` to make a prediction.
5.  **Mapping Output:** The model outputs a numerical prediction, which is mapped to its corresponding crop name using a dictionary.
6.  **Display Result:** The recommended crop name is sent back to the `home.html` template and displayed to the user.
* **`static/`**: This directory stores static assets like CSS for styling, JavaScript for interactivity, and images used in the frontend.
