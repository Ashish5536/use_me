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

st.write("2")
st.write("Harsh 25 26.5 28")
st.write("Anurag 26 28 30")
st.write("Harsh ")



st.write("Output: ")
st.write("26.50")
st.subheader("code:3")
st.code("""import numpy

# Step 1: Input लें और उसे integer में बदलें
n, m = map(int, input().split())

# Step 2: N पंक्तियों के लिए input पढ़ें और array बनाएँ
arr = numpy.array([ list(map(int, input().split())) for _ in range(n) ])

# Step 3: axis=0 पर sum करें (यानि कॉलम के अनुसार जोड़ें)
sum_result = numpy.sum(arr, axis=0)

# Step 4: उस sum_result का product निकालें
product_result = numpy.prod(sum_result)

# Step 5: अंतिम परिणाम प्रिंट करें
print(product_result)
""")

