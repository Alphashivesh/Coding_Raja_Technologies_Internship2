import streamlit as st
import pandas as pd

# Use session state to persist tasks across interactions
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.set_page_config(page_title="To-Do List App", page_icon="📝", layout="centered")

st.title("📝 To-Do List App")

# Input form
with st.form("task_form"):
    task = st.text_input("Task")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    due_date = st.date_input("Due Date")
    submitted = st.form_submit_button("➕ Add Task")

    if submitted and task:
        st.session_state["tasks"].append(
            {"task": task, "priority": priority, "due_date": str(due_date), "done": False}
        )
        st.success(f"Task '{task}' added!")

# Display tasks
st.subheader("📋 Your Tasks")

if st.session_state["tasks"]:
    df = pd.DataFrame(st.session_state["tasks"])
    for i, row in df.iterrows():
        cols = st.columns([4, 1, 1])
        status = "✅" if row["done"] else "❌"
        cols[0].write(f"{status} **{row['task']}** (Priority: {row['priority']}, Due: {row['due_date']})")

        if cols[1].button("Mark Done", key=f"done_{i}"):
            st.session_state["tasks"][i]["done"] = True
            st.experimental_rerun()

        if cols[2].button("🗑 Remove", key=f"remove_{i}"):
            st.session_state["tasks"].pop(i)
            st.experimental_rerun()
else:
    st.info("No tasks yet. Add some above ⬆️")
