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
st.subheader("code:2")
st.code("""# Read number of students
n = int(input())

# Create an empty dictionary to store student records
student_marks = {}

# Read n lines of student data
for _ in range(n):
    line = input().split()
    name = line[0]
    scores = list(map(float, line[1:]))
    student_marks[name] = scores

# Read the name to query
query_name = input()

# Calculate and print the average to 2 decimal places
average = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{average:.2f}")
""")
st.write("Input: ")

st.write(
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
")
st.write("Output: ")
st.write("26.50
")
