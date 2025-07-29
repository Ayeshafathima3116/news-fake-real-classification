# 📰 News Article Classification (Fake or Real)

This project uses machine learning and natural language processing (NLP) to classify news articles as either **Fake** or **Real**.

---

## 📌 Project Objective

To build a machine learning model that detects fake news using text classification techniques and deploy it as a user-friendly web application using **Streamlit**.

---

## 🚀 Tools & Technologies

- Python
- Pandas, NumPy
- Scikit-learn (Logistic Regression)
- NLTK (text preprocessing)
- TF-IDF Vectorizer
- Streamlit (app interface)
- Joblib (model saving/loading)

---


---

## 📥 Dataset

Dataset used from Kaggle:  
👉 [Fake and Real News Dataset on Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

**Note:** The full dataset is not included in this GitHub repo due to size limitations.  
To run the project, download both `Fake.csv` and `True.csv`, and place them in the `/data` folder.

---

## 🧠 Model Training Summary

1. Merged `Fake.csv` and `True.csv` from Kaggle.
2. Preprocessed text: lowercase, removed punctuation, stopwords using NLTK.
3. Converted text into vectors using TF-IDF.
4. Trained a **Logistic Regression** model.
5. Evaluated with **accuracy**, **F1-score**, and **confusion matrix**.
6. Saved the model and TF-IDF vectorizer using `joblib`.

---

## 💻 Run the App Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/news-fake-real-classification.git
cd news-fake-real-classification/app


