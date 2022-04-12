'''
output 
*     * 0, 6
 *   * 1, 5
  * * 2, 4
   * 3
  * *
 *   *
*     *
j = rows - 1 - i
i = j
else:
    " "
'''

rows = int(input("gimme rows: "))
for i in range(rows):
    for j in range(rows):
        if j == rows - 1 -i or j == i:
            print("*", end = "") 
        else:
            print(" ", end = "") #print spaces on the same line using end
    print()

'''
    for star in range(i):
        print("*" + " "  , end = " ") #print stars on ethe same line using end

    for star in range(2 * i - 1):
        print("* ", end = "") #print stars on ethe same line using end
    
    print() #printing empty line to skip a line'''