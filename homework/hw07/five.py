b = Heap(19)
b.display()
for e in range(18, 3, -1):
    b.insert(e)
    b.display()

def fun(node):
    answer = []
    currentLevel = [ node ]
    for n in currentLevel:
        print(n.key, end=' ')         # prints 4
        answer += [ n.key ]
    print()
    while not currentLevel == []: 
        newLevel = [] 
        for n in currentLevel: 
          if not n.left == None: newLevel += [ n.left]     
          if not n.right == None: newLevel += [ n.right ]
        currentLevel = newLevel
        for n in currentLevel:
            print(n.key, end=' ')         # prints 6 and 5
            answer += [ n.key ]
        print()
    return answer
