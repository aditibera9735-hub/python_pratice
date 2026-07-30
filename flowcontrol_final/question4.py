'''Ask the user to enter a word.
 Print the length of the word. 
 If the length is greater than 5, also print
   "That's a long '''

word = input("enter a word: ")
word_length = len(word)
print("length of the word is :",word_length)

if word_length > 5:
    print("thats a long word")