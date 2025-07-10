 📰 News Article Classification (Fake or Real)

This project uses machine learning and natural language processing (NLP) to classify news articles as either **Fake** or **Real**.

📌 Project Objective

To build a model that detects fake news using text classification and deploy it as a web app using Streamlit.

🚀 Tools & Technologies

- Python
- Pandas, NumPy
- Scikit-learn (Logistic Regression)
- NLTK (text preprocessing)
- TF-IDF Vectorizer
- Streamlit (app interface)
- Joblib (model saving)

 📁 Folder Structure

```
news-fake-real-classification/
├── app/                      # Streamlit app
│   └── app.py
├── data/                     # Raw datasets (Fake.csv, True.csv)
├── notebooks/                # Model training code (Jupyter notebook)
├── saved_models/             # Trained model and vectorizer
├── report.pdf                # Final  project report
├── README.md                 # Project overview and instructions
```

🧠 Model Training Steps

1. Merged Fake and Real news datasets from Kaggle.
2. Preprocessed text (lowercase, removed punctuation & stopwords).
3. Converted text into numerical format using TF-IDF.
4. Trained a Logistic Regression model.
5. Evaluated using accuracy and F1-score.
6. Deployed the model with a Streamlit UI.

💻 How to Run the App Locally

1. Clone the repo:
```bash
git clone https://github.com/your-username/news-fake-real-classification.git
cd news-fake-real-classification/app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

📄 Report

See `report.pdf` for summary, tools, steps, and conclusion.

✨ Output

<img width="1920" height="1080" alt="Screenshot 2025-07-10 212129" src="https://github.com/user-attachments/assets/62cfa1dd-f0b5-4552-a0bd-1e3fa5e4cbfb" />

<img width="1920" height="1080" alt="Screenshot 2025-07-10 213209" src="https://github.com/user-attachments/assets/cf3fdf06-e7be-403f-953f-54f31efd9d3f" />


📬 Contact

For queries, contact: 22am1a3116@svrec.ac.in
