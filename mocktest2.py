# Get user input for Length and Girth
Length = float(input("Please enter a Length: "))
Girth = float(input("Please enter a Girth: "))

# Calculator for fish weight
def add_fishweight(Girth, Length):
    weight = (Girth * Girth * Length) / 800
    return weight

fishweight = add_fishweight(Girth, Length)
print(f"The weight of the fish is: {fishweight} lbs")

# List the fish types and weight categories
def fish(): 
    fishlist = ["small fish", "medium fish", "big fish", "giant fish"]
    return fishlist

fishlist = fish()
print(f"Fish categories: {fishlist}")

def weight():
    weightlist = ["0 to 41 pounds", "42 to 99 pounds", "100 to 174 pounds", "> 175 pounds"]
    return weightlist

weightlist = weight()
print(f"Weight categories: {weightlist}")

# Categorize the fish based on its weight
def Fishsize(fishweight):
    if fishweight < 41:
        classification = "small fish"
    elif fishweight < 99:
        classification = "medium fish"
    elif fishweight < 174:
        classification = "big fish"
    else:
        classification = "giant fish"
    print(f"The fish is classified as a {classification}")

Fishsize(fishweight)
