import math # needed if we need random numbers

class Matrix:
    def __init__(self, map):                   # map comes in as a (multiline) string
        self.data = {}                         # data holds the map 
        self.letter = {}                       # letter helps with labeling of solution 
        count = 0                              # starts counting columns for width 
        for i in map:
            if not i == '\n':
                count += 1                     # count chars on the first line of map 
            else:
                break                          # stop on newline (assume map rectangular)
        self.width = count                     # write the number down as the width of the map 
        count = 0                              # starts counting this time the lines for height
        for i in map:
            if i == '\n':                      # now if we find a new line character 
                count += 1                     # we count it (so we count the lines) 
        self.height = count                    # at the end that's the height of the map 
        (line, column) = (0, 0)                # now we start in the top left corner
        for i in map:                          # and going through the (geographical) map 
            if not i == '\n':                  # store any legitimate character   
                self.data[line, column] = i    # in the data dictionary (as is) 
                column += 1                    # and as you progress increment column 
            else:                              # meanwhile a newline character increases line 
                (line, column) = (line + 1, 0) # and also indicates a reset for column 
        self.solution = []                     # here we reserve space for a solution (when/if we find it)
    # -- so at the end of this constructor we have initialized height, width and data as well as solution 
    def show(self):                                             # this function shows us the state of the matrix 
        josh = 0                                                # josh is a variable that helps us count steps in the solution 
        for elem in self.solution:                              # notice how for each element josh goes up by one 
            self.letter[elem] = chr(josh + 97)                  # we store these successive values of josh in letter
            josh += 1                                           # recall 'a' == 97, josh offsets that, then gets incremented
        print("--------------------")                           # showing starts with a horizontal line so we know where it does 
        for line in range(self.height):                         # for each line
            for column in range(self.width):                    # and for each column on that line 
                if (line, column) in self.solution:             # if the location (line, column) is on the solution path
                    print(self.letter[line, column], end=' ')   # print the letter that we assigned for that location earlier 
                else:                                           # if the location (line, column) is not on the solution path
                    print(self.data[line, column], end=' ')     # print a dot (.) or an X (obstacle) whatever is there in data 
            print()                                             # note how printing stays on the line; at the end print a newline 
        # -- so that takes care of printing the map (with the solution, if any, in it) 
        val = self.measure(self.solution)                       # measure the solution to print its length
        if val > 0 : print(val)                                 # but don't print if there is no solution yet
    # -- at the end of this function we see the map (as given) with the solution (if any is specified) drawn inside it
    def measure(self, path):                   # this function determines the length of a path 
        d = 0                                  # d accumulates the length, step by step 
        (line, column) = (0, 0)                # this is the starting point (top left corner) 
        for (l, c) in path:                    # now (l, c) goes through the path elements one by one
            dl = (l - line)                    # we calculate with Pythagoras; this is dy (vertical) 
            dc = (c - column)                  # this is dx (note we have (line, column) as previous)
            d += math.sqrt(dc*dc + dl*dl)      # this is the square of the sum of squares of dx and dy 
            (line, column) = (l, c)            # now make the current (l, c) previous and go get a new (l, c)
        return d                               # at the end we return d
# Interesting note: because of how we calculate the distance (on a discrete lattice) the following paths have same length:
# 
# 0 . . . . . . . . .     0 1 2 . . . . . . .     0 . . . . . . . . .     0 . . . . . . . . .     0 1 2 3 4 5 . . . .
# . 1 . . . . . . . .     . . . 3 . . . . . .     . 1 2 3 . . . . . .     . 1 . . . . . . . .     . . . . . . 6 . . .
# . 2 . . . . . . .     . . . . 4 . . . . .     . . . . 4 5 . . . .     . . 2 3 4 5 6 7 . .     . . . . . . . 7 . .
# . . 3 . . . . . .     . . . . . 5 . . . .     . . . . . . 6 7 8 .     . . . . . . . . 8 .     . . . . . . . . 8 . 
# . . . 4 5 6 7 8 9     . . . . . . 6 7 8 9     . . . . . . . . . 9     . . . . . . . . . 9     . . . . . . . . . 9
#
# Think about it: each has the length equal to 4 * math.sqrt(2) + 5 """
    def solve(self):
        self.solution = self.find()
    # -- at the end of this function solution contains a (possibly empty) solution as determined by find 
    def find(self):
        path = [(0, 0)] # [(0, 0), (1, 1), (2, 2), (1, 3), (2, 3), (3, 4), (4, 5), (3, 6), (3, 7), (4, 8), (4, 9)]
        return self.helper(path)
    # -- find relies on a helper function. Note sample solution built by hand in class which helper can recognize as a solution
    def helper(self, path):                                              # the focus of our attention for this final exam 
        if (path[-1] == (self.height-1, self.width-1)):                  # did we receive what looks like a valid solution? 
            return path                                                  # if so return it. We found it, we're done. 
        else:                                                            # otherwise try extending the path by one step
            (line, column) = path[-1]                                    # start by locating the last element in the path
            for j in [1, 0, -1]:                                         # then look through neighboring meridians (note order) and 
                for i in [1, 0, -1]:                                     # for each meridian thru neighboring latitudes (note order)                  
                    (nl, nc) = (line + i, column + j)                    # set coordinates for the candidate "neighbor": (nl, nc) 
                    if ((nl, nc) == (line, column) or \
                                                                         # if it's not a real neighbor we need to ignore it 
                        nl >= self.height or nl < 0 or  \
                                                                         # if the neighbor is in the ocean (two cases) also ignore
                        nc < 0 or nc >= self.width or     \
                                                                         # if neighbor is in canada or mexico also ignore it please
                        (nl, nc) in path or self.data[nl, nc] == 'X'):   # if neighbor has already been visited or is an obstacle ignore
                        pass                                             # so that's how we ignore it (only legitimate neighbors considered)
                    else:                                                # if the neighbor is in fact a new valid non-obstacle location 
                        # self.solution = path + [ (nl, nc) ]            # add neighbor to path and make path a solution for display purposes 
                        # self.show()                                    # show me where I'm at (this allows us to follow the search process)
                        result = self.helper(path + [ (nl, nc) ])        # and ask helper to pursue this path. Note we save what helper returns
                        if result == None:                               # if helper returns through the earlier pass result is a NoneType
                            pass                                         # so let's ignore it. We can print before a pass for tracing purposes 
                        else:                                            # but if the result is not empty it should be a path
                            if (result[-1] == (self.height-1, self.width-1)): 
                                return result                            # so if it's a solution we stop. Note we stop on the first solution we find.
                            else:                                        # 
                                pass                                     # if not, do we understand what happens?
    # Our original plan was (as described below): 
    #     (a) show a solution
    #     (b) find a solution (and show it)
    #     (c) find the best solution (and show it)
            
map1 = """\
..X.......
..X.......
.XX.......
..........
..........
"""

map2 = """\
..........
X..XXXXXX.
..XX.....X
....XXXXXX
..........
"""

map3 = """\
..X.
X.X.
.XX.
....
"""

for map in [map1, map2, map3]:
    a = Matrix(map)
    a.show()
    a.solve()
    a.show()
