import io
with io.open("production.txt", encoding="utf-8-sig") as f:
    production = f.read()
#print("Given Context Free Grammer:\n" ,production)

terminals = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nonTerminals = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
startSymbol = production[0]
first = {}
follow = {}

if startSymbol in nonTerminals:
    index = nonTerminals.index(startSymbol)
    nonTerminals.pop(index)
    #print(nonTerminals)  
    
occured_terminals = [char for char in production if char.isupper()]
finalTerminals = set(occured_terminals)
print(finalTerminals) 

if startSymbol in finalTerminals:
    

def first(string):
    firstSet = string.splitlines()
    #print(firstSet)        
    
    
first(production)