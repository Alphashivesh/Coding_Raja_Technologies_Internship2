import streamlit as st
import pandas as pd
import json
import os
from datetime import date

# --- File persistence ---
DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# --- Session State ---
if "tasks" not in st.session_state:
    st.session_state["tasks"] = load_tasks()
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

st.set_page_config(page_title="To-Do List App", page_icon="📝", layout="centered")

# --- Dark/Light Mode CSS ---
def set_theme(dark: bool):
    if dark:
        st.markdown(
            """
            <style>
            body { background-color: #121212; color: white; }
            .stTextInput>div>div>input, .stSelectbox>div>div>select {
                background-color: #1e1e1e !important;
                color: white !important;
            }
            .stButton>button { background-color: #333; color: white; }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            body { background-color: white; color: black; }
            .stTextInput>div>div>input, .stSelectbox>div>div>select {
                background-color: white !important;
                color: black !important;
            }
            .stButton>button { background-color: #eee; color: black; }
            </style>
            """,
            unsafe_allow_html=True,
        )

# --- Sidebar: Filters & Theme ---
st.sidebar.header("⚙️ Settings")
st.session_state["dark_mode"] = st.sidebar.toggle("🌙 Dark Mode", value=st.session_state["dark_mode"])
set_theme(st.session_state["dark_mode"])

st.sidebar.subheader("🔍 Filters")
filter_category = st.sidebar.multiselect("Filter by Category", ["Work", "Personal", "Shopping", "Other"])
filter_priority = st.sidebar.multiselect("Filter by Priority", ["Low", "Medium", "High"])
show_completed = st.sidebar.checkbox("Show Completed Tasks", value=True)
search_text = st.sidebar.text_input("Search Task")

# --- Main Title ---
st.title("📝 To-Do List App")

# --- Add Task Form ---
with st.form("task_form"):
    task = st.text_input("✍️ Task")
    priority = st.selectbox("⚡ Priority", ["Low", "Medium", "High"])
    category = st.selectbox("📂 Category", ["Work", "Personal", "Shopping", "Other"])
    due_date = st.date_input("📅 Due Date", min_value=date.today())
    submitted = st.form_submit_button("➕ Add Task")

    if submitted and task:
        st.session_state["tasks"].append(
            {
                "task": task,
                "priority": priority,
                "category": category,
                "due_date": str(due_date),
                "done": False,
            }
        )
        save_tasks(st.session_state["tasks"])
        st.success(f"Task '{task}' added!")

# --- Display Tasks ---
st.subheader("📋 Your Tasks")

tasks = pd.DataFrame(st.session_state["tasks"])

if not tasks.empty:
    # Apply filters
    if filter_category:
        tasks = tasks[tasks["category"].isin(filter_category)]
    if filter_priority:
        tasks = tasks[tasks["priority"].isin(filter_priority)]
    if not show_completed:
        tasks = tasks[tasks["done"] == False]
    if search_text:
        tasks = tasks[tasks["task"].str.contains(search_text, case=False)]

    completed = tasks["done"].sum()
    total = len(tasks)
    if total > 0:
        st.progress(completed / total)
        st.caption(f"✅ {completed} / {total} tasks completed")

    for i, row in tasks.iterrows():
        cols = st.columns([5, 1, 1, 1])
        status = "✅" if row["done"] else "❌"
        pri_color = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}[row["priority"]]

        cols[0].markdown(
            f"{status} **{row['task']}** ({pri_color} {row['priority']}, 📂 {row['category']}, ⏳ {row['due_date']})"
        )

        if cols[1].button("✔️", key=f"done_{i}"):
            st.session_state["tasks"][i]["done"] = True
            save_tasks(st.session_state["tasks"])
            st.rerun()

        if cols[2].button("✏️", key=f"edit_{i}"):
            with st.expander(f"Edit: {row['task']}"):
                new_task = st.text_input("Task", row["task"], key=f"edit_task_{i}")
                new_priority = st.selectbox("Priority", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(row["priority"]), key=f"edit_pri_{i}")
                new_category = st.selectbox("Category", ["Work", "Personal", "Shopping", "Other"], index=["Work", "Personal", "Shopping", "Other"].index(row["category"]), key=f"edit_cat_{i}")
                new_date = st.date_input("Due Date", pd.to_datetime(row["due_date"]).date(), key=f"edit_date_{i}")
                if st.button("💾 Save", key=f"save_{i}"):
                    st.session_state["tasks"][i] = {
                        "task": new_task,
                        "priority": new_priority,
                        "category": new_category,
                        "due_date": str(new_date),
                        "done": row["done"]
                    }
                    save_tasks(st.session_state["tasks"])
                    st.rerun()

        if cols[3].button("🗑", key=f"remove_{i}"):
            st.session_state["tasks"].pop(i)
            save_tasks(st.session_state["tasks"])
            st.rerun()
else:
    st.info("No tasks yet. Add some above ⬆️")
