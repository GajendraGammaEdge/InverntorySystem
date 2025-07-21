from ucimlrepo import fetch_ucirepo 
  

letter_recognition = fetch_ucirepo(id=59) 
  
X = letter_recognition.data.features 
y = letter_recognition.data.targets 
  

print(letter_recognition.metadata) 
  
print(letter_recognition.variables) 



