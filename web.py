import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # the selected pair is deleted from the session state dictionary
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=".", placeholder="Add Your new To-do...",
              on_change=add_todo, key="new_todo")

