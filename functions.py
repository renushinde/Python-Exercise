# A function is a repeatable process or procedure. Real world analogy will be a coffee machine. 
# Store and reuse pattern. DRY. A function is like a variable that holds a code. 
# In built funtions
import math
num1 = math.sqrt(81)
num2 = math.pow(8,4)
print(num1)
print(num2)

def mystery():
	toPrint =0
	for i in range(3):
		toPrint +=i

     print(toPrint)