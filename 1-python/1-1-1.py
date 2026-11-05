## INPUT and OUTPUT
name = input("Enter your name: ") 
print("Hello, World")
print("Hello, " + name + "!")

## FSTRINGS
print(f"Hello, {name}") # Same line Interpolated (fstring) 
print(f"{50} + {50} = {50 + 50}") # Interpolation evaluates these numbers to a value then prints that value 


## Type Detection and Conversion 

age = 20 # 20 is an INT literal so they type of age is going to be INT
gpa = 3.9 # 3.9 is a FLOAT so gpa is a FLOAT 

#type cohersion
age = int("99") # "99" is a string, putting INT makes it an INT 
print(age)

age = input("Enter your age: ") # This is type STR 
pass #basically says to do nothing (can put when using break points)
