# Coding_Raja_Technologies_Internship2

---

# 📝 Streamlit To-Do List App

This is a simple **To-Do List Web App** built using **Streamlit**.  
You can add tasks, assign priority & due date, mark tasks as done ✅, and remove tasks ❌.  

---

## 🚀 Live Demo  

Try the app here:  

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://codingrajatechnologiesinternship2-pf7jjkqrphdvmrzv3kzwqc.streamlit.app/)  

---

## 📌 Features
- ➕ Add new tasks with **priority** and **due date**  
- ✅ Mark tasks as **done**  
- ❌ Remove tasks  
- 🖥️ Runs on the browser with Streamlit  

---

## 🚀 Installation & Setup

1. **Clone this repository** (or copy the files):
   ```bash
   git clone https://github.com/yourusername/todo-streamlit.git
   cd todo-streamlit
   
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows

  
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the app**
   ```bash
   streamlit run app.py

---

## 🛠 Requirements
- Python 3.8+
- Streamlit

Install manually with:
```bash
   pip install streamlit
```

---

## 🌐 Deployment

You can deploy this project for free on:

### 🚀 Streamlit Cloud
1. Push your project to GitHub.  
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).  
3. Click **New App** → Connect your GitHub repo.  
4. Select the branch and `app.py` as the main file.  
5. Click **Deploy** 🎉  

---

### 🚀 Render
1. Push your project to GitHub.  
2. Go to [Render](https://render.com).  
3. Create a **New Web Service**.  
4. Select your repo and set:
   - **Build Command**:
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:
     ```bash
     streamlit run app.py --server.port $PORT --server.address 0.0.0.0
     ```
5. Deploy 🎉  

---

### 🚀 Heroku
1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).  
2. Create a `Procfile` in your project root:
   ```Procfile
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0


## 📧 Contact

For any questions, feedback, or collaboration inquiries, please feel free to reach out.

-   **Author**: [Shivesh Kumar]
-   **Email**: [shiveshkumar73520@gmail.com]
-   **GitHub**: [@alphashivesh](https://github.com/alphashivesh)

   
