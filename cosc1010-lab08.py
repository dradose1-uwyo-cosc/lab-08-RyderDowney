# Ryder Downey
# UWYO COSC 1010
# Submission Date: 11/5/2024
# Lab 08
# Lab Section: 14
# Sources, people worked with, help given to: John Jones, Google AI showed me how to input the math function for the sqrt
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert_string(s):
    """Function to convert strings into integers or floats"""
    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()): #checks if string is an integer
        return int(s)
    elif s.count('.') == 1: #checks if the string is a float with only one decial point
        left, right = s.split('.') #removes the . from the float
        if (left.isdigit() or (left.startswith('-') and left[1:].isdigit())) and right.isdigit(): #checks if both sides are digits and for if there is a negative sign present
            return float(s)
    return False #returns for if the input cant be converted into an integer or float

print("*" * 75)

def convert_string(s):
    """Function to convert strings into floats or integers if possible"""
    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()): #checks if the string is an integer (including negatives)
        return int(s)
    elif s.count('.') == 1: #checks for a float with one decimal point
        left, right = s.split('.') #removes the decimal point from the string
        if (left.isdigit() or (left.startswith('-') and left[1:].isdigit())) and right.isdigit(): #checks for negative sign using string indexing
            return float(s)
    
    # If it can't be converted, return False
    return False


def slope_intercept(m, b, x_lower, x_upper): #defines each value in the slope intercept form
    """Function to calculate a list of Y values for the given m, b, x_lower, x_upper"""
    if not (isinstance(x_lower, int) and isinstance(x_upper, int)) or x_lower > x_upper: #ensures that x_lower and x_upper are integers and the x_lower is less than x_upper
        return False
    
    y_values = []#creates a list for the outputted y values
    for x in range(x_lower, x_upper + 1): #inclusive range of x values
        y = m * x + b #slope intercept formula
        y_values.append(y) #appends the calculated y value into the y_values list
    
    return y_values

#end of setup parameter functions
#beginning of main functions

while True:
    user_input = input("Enter 'm b x_lower x_upper' or type 'exit' to quit: ").strip()
    if user_input.lower() == 'exit': #creates a value to end the loop
        print("Exiting the program.")
        break

    try:
        m_str, b_str, x_lower_str, x_upper_str = user_input.split() # Splits and converts each value of the formula into integers using the convert_string function
        m = convert_string(m_str)
        b = convert_string(b_str)
        x_lower = convert_string(x_lower_str)
        x_upper = convert_string(x_upper_str)

        if m is False or b is False or x_lower is False or x_upper is False: # Check if conversion was successful for each input (i.e. checks if convert_string returns false)
            print("Invalid input: please enter numbers only (e.g., '2 3 0 5').") #notifies the user that they incorrectly input something
            continue

        result = slope_intercept(m, b, x_lower, x_upper) #initiates the slope_intercept function and runs the user given numbers
        if result is False: #paremeters for if the interval is wrong
            print("Invalid bounds. Make sure x_lower is less than or equal to x_upper and both are integers.")
        else:
            print("Y values for each x in range:", result) #outputs the list of y integers
    except ValueError: #accounts for value error and notfies the user
        print("Invalid format. Please enter four numbers (e.g., '2 3 0 5').")
# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("*" * 75)

import math #imports math functions (in this case square root for the quadratic equation)

def quadratic_formula(a, b, c): #defines the values needed for the quadratic formula
    """Solve the quadratic equation using quadratic formula"""
    discriminant = b**2 - 4 * a * c
    if discriminant < 0: #verifies that the discriminant (inside the square root) isn't negative
        return None #if the discriminant is negative then there are no solutions/zeros
    sqrt_discriminant = math.sqrt(discriminant) #uses the math square root function with the discriminant
    # Calculates the two roots because of the +/- within the quadratic formula
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    return root1, root2

#end of setup parameter functions
#beginning of main user input code

while True:
    user_input = input("Enter coefficients 'a b c' or 'exit' to quit: ")
    if user_input.lower() == 'exit': #exit parameters
        break
    try:
        a, b, c = map(float, user_input.split()) #splits and converts the inputs to floats
        result = quadratic_formula(a, b, c) #calls the quadratic formula for the given user inputs
        if result is None: # parameters for if there are no real solutions (if the discriminant is negative)
            print("No real solutions.")
        else:
            print(f"The solutions are: x = {result[0]}, x = {result[1]}") #outputs two results because of the +/- in the formula
    except: #accounts for user error
        print("Invalid input, please enter three numbers.")
# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
