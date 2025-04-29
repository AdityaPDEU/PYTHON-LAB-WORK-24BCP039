class matrix:
    def __init__ (self,data):
        self.data=data
        self.row=len(data)
        self.col=len(data[0]) if data else 0
    def print_matrix(self):
        for row in self.data:
            print(row)
    def __add__(self,other):
        if self.row != other.row or self.col!= other.col:
            print("Addition not possible: Matrix dimensions do not match.")
            return None
        result=[]
        for i in range(self.row):
            row=[]
            for j in range (self.col):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return matrix(result)

m1 = matrix([[1, 2, 5], [3, 4, 7], [4, 8, 6]])
m2 = matrix([[5, 6, 4], [7, 8, 4], [5, 2, 3]])

print("Matrix 1:")
m1.print_matrix()

print("\nMatrix 2:")
m2.print_matrix()

# Add the matrices
print("\nSum of Matrices:")
m3 = m1 + m2
if m3:
    m3.print_matrix()

