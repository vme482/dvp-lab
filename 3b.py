from difflib import SequenceMatcher
s1=input("Enter the first String")
s2=input("Enter the second String")
print(SequenceMatcher (None,s1,s2).ratio())