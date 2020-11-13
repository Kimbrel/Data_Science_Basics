# DAY 1

'''
Questions 1:
Given the following jumbled word, OBANWRI guess the correct English word.
A.RANIBOW
B.RAINBOW
C.BOWRANI
D.ROBWANI

Answer: B

'''
#Question 2

print('"LETS UPGRADE"')

# Question 3

costPrice = input()
costPrice = float(costPrice)
sellingPrice = input()
sellingPrice = float(sellingPrice)
if (costPrice < sellingPrice):
    print("Profit")
elif (costPrice > sellingPrice):
    print('Loss')
else:
    print('Neither')
    
# Question 4

Euro = input()
Euro = float(Euro)
rupees = Euro * 80
print(rupees)
