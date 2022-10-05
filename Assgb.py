class Assignment8:
    #1.	Write a Python Program to Add Two Matrices?
    def Add_Two_Matrices(self):
        x = list(eval(input("Enter the first metrix")))
        y= list(eval(input("Enter the secound metrix")))
        result = [[0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(x)):
            for j in range(len(x[0])):
                result[i][j] = x[i][j] + y[i][j]
        for r in result:
            print(r)

    #2.	Write a Python Program to Multiply Two Matrices?
    def Multiply_Two_Matrices(self):


a = Assignment8
a.Add_Two_Matrices
print(a.Add_Two_Matrices(""))