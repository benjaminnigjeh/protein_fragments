import streamlit as st
import protein_fragments
from protein_fragments import utils

def main():
    st.title("Simple Streamlit App")
    st.write("This is a simple Streamlit app.")

    # User inputs
    name = st.text_input(utils.hello())
    age = st.number_input(utils.goodbye())

    # Display greeting message
    if name:
        st.write(f"Hello, {name}!")
        if age:
            st.write(f"Your age multiplied by 2 is: {age * 2}")

if __name__ == "__main__":
    main()
