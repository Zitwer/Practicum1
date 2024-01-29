# Rebecca Zitwer
# Assignment 1  

# Get the user input 
userInput = input("Enter a string with numbers: ")

# Call method to replace the number with words
def replaceWithWord(userInput):
    numbers = {
         0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
        30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    words = userInput.split()

# Loop through the words to find a number to convert
    for item in words:
       if item.isnumeric() and int(item) < 100:
           
           string_number = ""
           # If the number is greater then 20, get the remainder when divided by 10
           # Get the corresponding name to the whole number and corresponding name to the remainder (1-9)
           if int(item) > 20:
               remainder = int(item) % 10
               regular = int(item) // 10 * 10
               string_number += numbers[regular]
               if remainder > 0:
                string_number += "-" + numbers[remainder]
           # If the number is less than 20 get the corresponding name
           else:
               string_number = numbers[int(item)]
           # Replace the number with the string value
           userInput = userInput.replace(item, string_number)

    # Display the results
    print("Output: " )
    print(userInput)

# Call the method 
replaceWithWord(userInput)
