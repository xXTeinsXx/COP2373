# Programming Exercise 7
# be able to accurate count the amount of sentences in a text or paragragh user inputs

# Importing the regular expression library
import re 

# Checks to see if the user wants to run the code
def runcode():
    runcode = str(input("Do you want to run thid code? (y/n): "))
    return runcode.casefold()

# Function that takes the user input and counts the amount of sentences in the text
def main():
    text = str(input("Enter the text you want to count the sentences in: "))
    pattern = r'[A-Z].*?[.!?](?=[A-Z]|$)'
    sentences = re.findall(pattern, text, flags=re.DOTALL | re.MULTILINE)
    
    for i in sentences:
        print('->',i)
    
    print(f"The amount of sentences in the text is: {len(sentences)}")


# Asks the user if they want to run the code
while runcode() == "y":
    main()

# If the user doesn't want to run the code, the program will end    
else:
    print('Goodbye! 👋 See you next time!')