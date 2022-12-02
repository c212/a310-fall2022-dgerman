class Matrix:
    def __init__(self, map):
        self.data = {}
        self.letter = {}
        count = 0 # count the columns
        for i in map:
            if not i == '\n':
                count += 1
            else:
                break
        self.width = count
        count = 0 # count the lines
        for i in map:
            if i == '\n':
                count += 1
        self.height = count
        (line, column) = (0, 0)
        for i in map:
            if not i == '\n':
                self.data[line, column] = i
                column += 1
            else:
                (line, column) = (line + 1, 0)
        self.solution = []
    def show(self):
        print("--------------------")
        for line in range(self.height):
            for column in range(self.width):
                if (line, column) in self.solution:
                   print(self.letter[line, column], end=' ')
                else:
                   print(self.data[line, column], end=' ')
            print()
    def solve(self):
        self.solution = self.find()
        josh = 0
        for elem in self.solution:
            self.letter[elem] = chr(josh + 65)
            josh += 1
    def find(self):
        path = [(0, 0)] # [(0, 0), (1, 1), (2, 2), (1, 3), (2, 3), (3, 4), (4, 5), (3, 6), (3, 7), (4, 8), (4, 9)]
        return self.helper(path) 
    def helper(self, path):
        if (path[-1] == (self.height-1, self.width-1)):
            return path
        else:
            (line, column) = path[-1]
            for j in [-1, 0, 1]:
                for i in [-1, 0, 1]:
                    # look at (line + i, column + j) except when (i, j) = (0, 0)
                    (nl, nc) = (line + i, column + j)
                    if ((nl, nc) == (line, column) or \
                        (nl, nc) in path or self.data[nl, nc] == 'X' or \
                        nl >= self.height or nl < 0 or nc < 0 or nc >= self.width):
                        pass
                    else:
                        # legitimate neighbor (possibly)
                        print (path + [ (nl, nc) ])
                        return self.helper(path + [ (nl, nc) ])                    

    #1 show a solution
    #2 find a solution (and show it)
    #3 find the best solution (and show it)
            
map = """\
.......X..
.......X..
....XXXX..
..........
..........
"""
a = Matrix(map)
a.show()
a.solve()
a.show()
















