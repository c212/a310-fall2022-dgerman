class Heap:
  def __init__(self, key):
    self.key = key
    self.right = None
    self.left = None
    
# lab code starts here ------------------------------------------------(09/22/2023)----------

  def remove(self):
    path = "{0:b}".format(self.size())
    value = self.helper(path[1:])
    self.key = value
    # cut that from the tree
    p = self
    last = path[-1]
    for c in path[1:-1]:
      # print(c)
      if c == "0":
        p = p.left
      else:
        p = p.right
    if last == "0":
      p.left = None
    else:
      p.right = None
    self.clean()
    return self

  def clean(self):
    if self.left == None and self.right == None:
      pass
    elif self.right == None:
      if self.key > self.left.key:
        (self.left.key, self.key) = (self.key, self.left.key)
        # self.left.clean()
    else:
      if self.key <= self.left.key and self.key <= self.right.key:
        pass
      if self.left.key < self.right.key:
        (self.left.key, self.key) = (self.key, self.left.key)
        self.left.clean()
      else:
        (self.right.key, self.key) = (self.key, self.right.key)
        self.right.clean()

  def helper(self, path):
    # print(path, self.key)
    if path == "1": return self.right.key
    elif path == "0": return self.left.key
    else:
      nextStep = path[0]
      if nextStep == '0':
        return self.left.helper(path[1:])
      else:
        return self.right.helper(path[1:])
    
  def removeOld(self):                                  # this is the code we added in class
# lab code ends here --------------------------------------------------(09/22/2023)----------
    if self.right == None and self.left == None:        #
      return None                                       #
    elif self.right == None:                            #
      return self.left                                  #
    else:                                               #
      if (self.left.key < self.right.key):              #
        self.key = self.left.key                        #
        self.left = self.left.remove()                  #
        return self                                     #
      else:                                             #
        self.key = self.right.key                       #
        self.right = self.right.remove()                #
        return self                                     # 
  def size(self):
    if self.left == None and self.right == None:
      return 1
    elif self.left == None:
      return 1 + self.right.size();
    elif self.right == None:
      return 1 + self.left.size()
    else: 
      return 1 + self.right.size() + self.left.size()
  def depth(self):
    if self.left == None and self.right == None:
      return 1
    elif self.left == None:
      return 1 + self.right.depth();
    elif self.right == None:
      return 1 + self.left.depth()
    else: 
      return 1 + max(self.right.depth(), self.left.depth())
  def insert(self, key):
    if self.left == None and self.right == None:
      self.left = Heap(key)
      if self.left.key < self.key: # [1] -----------------------------------------------------
        (self.left.key, self.key) = (self.key, self.left.key)
    elif self.right == None:
      self.right = Heap(key)
      if self.right.key < self.key: # [2] ----------------------------------------------------
        (self.right.key, self.key) = (self.key, self.right.key)
    else:
      leDe = self.left.depth()
      leSi = self.left.size()
      riDe = self.right.depth()
      riSi = self.right.size()
      if leSi < 2 ** leDe - 1:
        self.left.insert(key)
        if self.left.key < self.key: # [1] ---------------------------------------------------
          (self.left.key, self.key) = (self.key, self.left.key)
      elif leSi == (2 ** leDe - 1) and riSi < leSi:
        self.right.insert(key)
        if self.right.key < self.key: # [2] --------------------------------------------------
          (self.right.key, self.key) = (self.key, self.right.key)
      else:
        self.left.insert(key)
        if self.left.key < self.key: # [1]
          (self.left.key, self.key) = (self.key, self.left.key)
  def display(self):
    lines, *_ = self._display_aux()
    for line in lines:
      print(line)
  def _display_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
      line = '%s' % self.key
      width = len(line)
      height = 1
      middle = width // 2
      return [line], width, height, middle
    # Only left child.
    if self.right is None:
      lines, n, p, x = self.left._display_aux()
      s = '%s' % self.key
      u = len(s)
      first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
      second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
      shifted_lines = [line + u * ' ' for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
    # Only right child.
    if self.left is None:
      lines, n, p, x = self.right._display_aux()
      s = '%s' % self.key
      u = len(s)
      first_line = s + x * '_' + (n - x) * ' '
      second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
      shifted_lines = [u * ' ' + line for line in lines]
      return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
    # Two children.
    left, n, p, x = self.left._display_aux()
    right, m, q, y = self.right._display_aux()
    s = '%s' % self.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
      left += [n * ' '] * (q - p)
    elif q < p:
      right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2

def removeTop(heap):            # these are the two wrappers that I added just now (after the lab)  
  if heap == None:              # they would not be necessary if we used the null object design pattern 
    return None                 #
  elif heap.left == heap.right == None:
    return None
  else:                         #
    return heap.remove()        #
                                #
def display(heap):              #
  if heap == None:              #
    print(None)                 #
  else:                         #
    heap.display()              # please also see how these are called in the tests below

import random

b = Heap(1)
b.display()
for _ in [2, 3, 7, 5, 6]:
  print("----------------( now inserting " + str(_) + " )--")
  b.insert(_)
  b.display()                   # so far so good (there was no chance of None thus far)  
for _ in range(7):
  print("Removing top of heap now ... heap becomes:" )
  b = removeTop(b)
  display(b)
  
