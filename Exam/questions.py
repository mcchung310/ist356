import streamlit as st
from figures import *

# if vs elif example 

grade = st.text_input("Enter your letter grade: ")

message = ""

if grade == "A":
    message = "Excelent work!"
elif grade == "B":
    message = "Good Job!"
elif grade == "C":
    message = "You can do better!"
else:
    message= "Invalid grade. Please enter A, B, or C."


st.dataframe(df1)

# Question 24
output = df1.apply(lambda row: row['COLB'] + row['COLC'], axis=1).sum()
st.write(output)

# Merges (df1 and df2)
output1 = pd.merge(df1, df2, how="right",left_on="COLA", right_on="COLE")
st.write(output1)

# Concat (df2 and df3)
output3 = pd.concat([df2, df3])
st.write(output3)

output4 = pd.concat([df1, df2])
st.write(output4)

# Pivot df8 (UNFINISHED)
output4 = df8.pivot(index="COLA", columns="COLB", )
st.write(output4)

# Question 63 (counts - does not count NaN's)
output5 = df1['COLC'].count()
st.write(output5)

s = "this is a test"
print(s.find("zzz"), s.count("is"))
print(s.find("a"), s.count("no"))
print(s.find("test"), s.count("s"))

x = 35
if x > 20:
    print ("Yay")
elif x >25:
    print ("Horray")
if x > 30:
    print ("Awesome")


a = {"x": 1, "y": 2}
print(a)

b = dict(name="Sam", age=20)
print(b)


text = "30 40 90 10"
tokens = text.split() # line A
numbers = [int(t) for t in tokens] # line B
total = sum(numbers) # line C
print(f"{tokens}, {numbers}, {total}")

x = "jonathan myers"
print(x[2:5:1])

name = "Jonathan Myers"
course = "microbio"
print(f"Hey {name}, how was {course}!")


for i in range(2, 8):
    print(i)

for ch in "testing":      # "testing" is the iterable
    print(ch)

for n in [10, 20, 30]:    # the list is the iterable
    print(n)

while True:
    raw = input("Enter a number or type 'stop':")
    if raw == 'stop':
        break

int(4.5)
