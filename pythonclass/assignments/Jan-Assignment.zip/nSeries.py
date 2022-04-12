#Marina Tanaka
'''
calculate the sum of series up to n term. 
For example, if n = 5 the series will become 
2 + 22 + 222 + 2222 + 22222 = 24690
'''
import math

n = int(input("Gimme a number: ")) + 1
#starts from 0 so add 1 to get the series to start from 2

formula = math.ceil(0.0246 * (math.pow(10, n) - 1 - (9 * n)))
#formula is from the internet so plug the n in 
#ceil ronuds the float to the next integer. It can be round()

print(formula)

'''
S = 2(1 + 11 + 111...)
  = 2/9(9 + 99 + 999...)
  = 2/9(10 ** 1 - 1 + ... + 10 ** n - 1)
  = 2/9()
'''
for i in range(1, n + 1):
   