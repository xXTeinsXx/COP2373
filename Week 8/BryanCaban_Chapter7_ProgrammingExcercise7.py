# Programming Exercise 7 v2
# Be able to accurately count the amount of sentences in a text or paragraph user inputs, including sentences that begin with numbers

# Importing the regular expression library
import re 

# Checks to see if the user wants to run the code
def runcode():
    runcode = str(input("Do you want to run this code? (y/n): "))
    return runcode.casefold()

# Function that extracts sentences from text
def extract_sentences(text):
    # Pattern to match sentences starting with letters or numbers
    pattern = r'(?:[A-Z0-9][^.!?]*?[.!?])'
    sentences = re.findall(pattern, text)
    return sentences

# Function that displays each sentence
def display_sentences(sentences):
    for i in sentences:
        print('->', i)
    
    # Print the total count of sentences
    print(f"The amount of sentences in the text is: {len(sentences)}")

# Function that takes the user input and processes the text
def main():
    text = str(input("Enter the text you want to count the sentences in: "))
    sentences = extract_sentences(text)
    display_sentences(sentences)

# Asks the user if they want to run the code
while runcode() == "y":
    main()

# If the user doesn't want to run the code, the program will end    
else:
    print('Goodbye! 👋 See you next time!')