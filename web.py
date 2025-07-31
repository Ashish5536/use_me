import streamlit as st
name = st.text_input("Enter your name: ")
st.header("Python")
st.subheader("code:1")
st.code("""if __name__ == '__main__':
    n = int(input())                        # Read number of scores
    arr = list(map(int, input().split()))  # Read scores and convert to list of integers
    unique_scores = list(set(arr))         # Remove duplicates
    unique_scores.sort(reverse=True)       # Sort in descending order
    print(unique_scores[1])                # Print the second highest score
""")
st.write("Input: ") 
st.write("5")
st.write("2 3 6 6 5")
st.write("Output: ")
st.write("5")
