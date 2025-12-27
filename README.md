# 🧠 Full Stack AI Journey

Welcome to the **Full Stack AI** repository! This project represents a comprehensive learning path from the fundamentals of Python programming to advanced Machine Learning algorithms, Natural Language Processing (NLP), and Model Deployment.

---

## 📂 Project Roadmap

This repository is organized into modules focusing on specific stages of AI development.

### 🔹 Week 1: Foundations & Analysis
*   **Python Basics:** Variables, Data Types, Operators, Control Flow (If/Else, Loops).
*   **Data Structures:** Lists, Tuples, Sets, Dictionaries.
*   **Core Libraries:** Introduction to **Numpy** and **Pandas** for data manipulation.
*   **Visualization:** Plotting basics with **Matplotlib**.
*   **File Handling:** Reading/Writing files and Exception Handling.

### 🔹 Week 2: Data Science & ML Essentials
*   **EDA (Exploratory Data Analysis):** Deep dive with Seaborn.
*   **Preprocessing:** Scaling (MinMax, Robust), Encoding (Label, One-Hot), and Binarization.
*   **Supervised Learning (Regression):** Linear, Multiple Linear, Polynomial, Lasso, Ridge, and ElasticNet.
*   **Supervised Learning (Classification):** Logistic Regression, Naive Bayes, Decision Trees.
*   **Validation:** Cross-Validation techniques.

### 🔹 Week 3: Advanced ML & Deployment
*   **Advanced Algorithms:** SVM (SVC/SVR), KNN, Decision Tree Regression.
*   **Unsupervised Learning:** Clustering (K-Means, Hierarchical), PCA.
*   **Optimization:** Feature Selection, Outlier Detection, Hyperparameter Tuning.
*   **Ensemble Methods:** Bagging, Boosting.
*   **Deployment:** Serving models using **Flask** and **FastAPI**.

### 🔹 Week 5 & 6: NLP & Database Management
*   **Natural Language Processing:** Bag of Words (BoW), TF-IDF, Word2Vec, Sentiment Analysis, Language Detection.
*   **SQL Mastery:** ER Diagrams, Joins, Stored Procedures, Triggers, Views.

### 🛠️ Utilities
*   **PDF Tools:** A dedicated script (`pdf_to_img.ipynb`) to extract images from PDF documents using PyMuPDF.

---

## 📦 Dependencies & Packages

To run the notebooks and scripts in this repository, you will need the following Python libraries.

| Package | Purpose |
| :--- | :--- |
| `numpy` | Numerical computing and array processing. |
| `pandas` | Data manipulation and analysis (CSV handling). |
| `matplotlib` | Data visualization and plotting. |
| `seaborn` | Statistical graphics. |
| `scikit-learn` | Machine learning algorithms and preprocessing tools. |
| `scipy` | Scientific computing (needed for sparse matrices/stats). |
| `pymupdf` | PDF processing (listed as `fitz` in imports). |
| `pillow` | Image processing (PIL). |
| `flask` | Web framework for deploying ML models. |
| `fastapi` | Modern web framework for building APIs. |
| `uvicorn` | ASGI server for running FastAPI. |
| `joblib` | Saving and loading trained models. |
| `nltk` | Natural Language Processing toolkit. |

---

## ⚙️ Installation & Setup

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository
Download the project to your local drive.
bash git clone <repository-url> cd "Full Stack AI"

### 2. Create a Virtual Environment (Recommended)
It is best practice to run this project in an isolated environment.

**Windows:**
bash python -m venv venv .\venv\Scripts\activate

**macOS / Linux:**
bash python3 -m venv venv source venv/bin/activate

### 3. Install Required Packages
Run the following command to install all necessary libraries:
bash pip install numpy pandas matplotlib seaborn scikit-learn scipy pymupdf pillow flask fastapi uvicorn joblib nltk

### 4. Database Setup (Optional)
For the SQL sections in Week 5/6, ensure you have **MySQL** installed. The project includes `dataSources.xml` configured for a local connection:
*   **Driver:** MySQL Connector
*   **URL:** `jdbc:mysql://localhost:3306`

---

## 🖥️ Usage

### Running Jupyter Notebooks
To explore the lessons and assignments, start the Jupyter Lab or Notebook server:
bash jupyter notebook
Navigate to specific folders (e.g., `week2/w2_s7/Session 7/`) to open `.ipynb` files.

### Running the PDF Tool
To extract images from a PDF, open `pdf_to_img.ipynb`. Ensure you have a `temp/extracted_images` directory or allow the script to create it.
python
Example usage inside the notebook
extract_images_from_pdf("path/to/your/document.pdf")

### Deploying Models
To run the deployment examples in `week3/w3_s16/`:

**Flask:**
bash cd "week3/w3_s16/flask deploy model" python app.py

**FastAPI:**
bash cd "week3/w3_s16/fastAPI deploy model" uvicorn main:app --reload

---

## 🤝 Contributing
Feel free to submit issues or pull requests if you find bugs or want to add more advanced AI modules!

---
*Generated for the Full Stack AI Course.*
