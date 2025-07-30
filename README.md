# Animal Health Classification Web App

This project is an AI-driven initiative to assess an animal's health status. By analyzing a set of symptoms, the machine learning model predicts whether the animal's condition is 'Critical' or 'Normal'. This tool provides a simple web interface for users to input symptoms and receive an immediate, data-backed health assessment.

---
## Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, Pandas, Imbalanced-learn
- **Environment:** uv, Jupyter

---
## Setup and Running the Project

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites

- Python 3.11
- [uv](https://github.com/astral-sh/uv) (a fast Python package installer)

### 2. Clone the Repository
Clone this project to your local machine.
```bash
git clone https://github.com/deshmukh-sakshi/AnimalHealthClassifier.git
cd AnimalHealthClassifier
```

### 3. Create Virtual Environment
Create a dedicated virtual environment for the project using uv.
```bash
uv venv .venv
```

### 4. Activate the Virtual Environment & Install Dependencies
Activate the virtual environment.
- On Windows:
```bash
.venv\Scripts\activate
```
- On macOS/Linux:
```bash
source .venv/bin/activate
``` 
Install the required dependencies.
```bash
uv pip install flask pandas numpy jupyter scikit-learn imbalanced-learn
```

### 5. Generate the Model
The machine learning model needs to be trained first. This step reads the Animal_Health.csv, trains the model, and creates the rfc.pkl and scaler.pkl files.
```bash
jupyter nbconvert --to notebook --execute Animal_Health_Classification.ipynb
```

### 6. Run the Web App
You can now start the Flask web server.

```bash
python app.py
```

Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the application.