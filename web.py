import streamlit as st
import functions


def add_todo():
    # It's like a dictionary that allows us to get value from the input box
    todo = st.session_state['new_todo'].capitalize() + '\n'
    if todo not in todos:
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state['new_todo'] = ""


todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my To-Do App")
st.write("This app is made to help you stay organized and increase your productivity.")

for index, to_do in enumerate(todos):
    checkbox = st.checkbox(to_do, key=index)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new to-do...", key="new_todo", on_change=add_todo)
