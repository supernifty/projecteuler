
# item consists of { 'root': value, 'left': item or None, 'right': item or None, 'best': value or None }
def best(tree):
  if 'left' not in tree and 'right' not in tree: # leaf
    return tree['root']
  
  if 'left' not in tree:
    return tree['root'] + best(tree['right'])

  if 'right' not in tree:
    return tree['root'] + best(tree['left'])

  # both children present
  return tree['root'] + max( best(tree['left']), best(tree['right']) )

def make_tree(ns):
  levels = []
  level = 0
  pos = 0
  levels.append([])
  for n in ns:
    tree = { 'root': n }
    levels[level].append( tree )
    # connect to higher level
    if level > 0:
      if pos < level:
        levels[level-1][pos]['left'] = tree
      if pos > 0:
        levels[level-1][pos-1]['right'] = tree
    pos += 1
    if pos == level+1:
      level += 1
      pos = 0
      levels.append([])
  return levels[0][0]

#tree = make_tree( [ 3, 7, 4, 2, 4, 6, 8, 5, 9, 3 ] )
tree = make_tree( [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 04, 82, 47, 65, 19, 01, 23, 75, 03, 34, 88, 02, 77, 73, 07, 63, 67, 99, 65, 04, 28, 06, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23] )
#print tree

print best(tree)
