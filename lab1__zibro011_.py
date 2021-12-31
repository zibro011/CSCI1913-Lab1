def left(e):
    return e[0]
def op(e):
    return e[1]
def right(e):
    return e[2]

def isInside(v, e):
    if v == e:
        return True
    if type(e) == tuple:
        if isInside (v,left(e)):
            return True
        elif isInside (v,right(e)):
            return True
        else:
            return False
    else:
        return False

def solve(v, q):
    if v == q:
        return q
    if isInside (v,left(q)):
        return solving(v,q)
    elif isInside (v,right(q)):
        reversed = (right(q), op(q), left(q))
        return solving(v,reversed)
    else:
        return None

def solving(v, q):
    if v == left(q):
        return q
    elif op(left(q))=='+':
        return solvingAdd(v,q)
    elif op(left(q))=='-':
        return solvingSubtract(v,q)
    elif op(left(q))=='*':
        return solvingMultiply(v,q)
    elif op(left(q))=='/':
        return solvingDivide(v,q)

def solvingAdd(v,q):
    if isInside(v,left(left(q))):
        q_prime = ( left(left(q)) , '=' , (right(q),'-', right(left(q))))
        return solving(v,q_prime)
    elif isInside(v, right(left(q))):
        q_prime = (right(left(q)), '=' , (right(q),'-',left(left(q))))
        return solving(v,q_prime)

def solvingSubtract(v,q):
    if isInside (v,left(left(q))):
        q_prime = (left(left(q)), '=', ((right(q)), '+', right(left(q))))
        return solving(v,q_prime)
    elif isInside(v, right(left(q))):
        q_prime =( right(left(q)) , '=' , (left(left(q)),'-', right(q)))
        return solving(v,q_prime)

def solvingMultiply(v,q):
    if isInside (v,left(left(q))):
        q_prime = ( left(left(q)) , '=' , (right(q),'/', right(left(q))))
        return solving(v,q_prime)
    elif isInside(v, right(left(q))):
        q_prime = (right(left(q)), '=' , (right(q),'/',left(left(q))))
        return solving(v,q_prime)

def solvingDivide(v,q):
    if isInside (v,left(left(q))):
        q_prime = (left(left(q)), '=', ((right(q)), '*', right(left(q))))
        return solving(v,q_prime)
    elif isInside(v, right(left(q))):
        q_prime =( right(left(q)) , '=' , (left(left(q)),'/', right(q)))
        return solving(v,q_prime)

#
#  TESTS. Test the equation solver for CSci 1913 Lab 1.
#
#    James Moen
#    10 Sep 18
#
#  Every test is followed by a comment which shows what must be printed if your
#  code works correctly. It also shows how many points the test is worth, for a
#  total of 35 possible points.
#

print(isInside('x', 'x'))                          #  True   1 point
print(isInside('x', 'y'))                          #  False  1 point
print(isInside('x', ('x', '+', 'y')))              #  True   2 points
print(isInside('x', ('a', '+', 'b')))              #  False  2 points
print(isInside('+', ('a', '+', 'b')))              #  False  2 points
print(isInside('x', (('m', '*', 'x'), '+', 'b')))  #  True   2 points

print(solve('x', (('a', '+', 'x'), '=', 'c')))
#  ('x', '=', ('c', '-', 'a'))  2 points

print(solve('x', (('x', '+', 'b'), '=', 'c')))
#  ('x', '=', ('c', '-', 'b'))  2 points

print(solve('x', (('a', '-', 'x'), '=', 'c')))
#  ('x', '=', ('a', '-', 'c'))  2 points

print(solve('x', (('x', '-', 'b'), '=', 'c')))
#  ('x', '=', ('c', '+', 'b'))  2 points

print(solve('x', (('a', '*', 'x'), '=', 'c')))
#  ('x', '=', ('c', '/', 'a'))  2 points

print(solve('x', (('x', '*', 'b'), '=', 'c')))
#  ('x', '=', ('c', '/', 'b'))  2 points

print(solve('x', (('a', '/', 'x'), '=', 'c')))
#  ('x', '=', ('a', '/', 'c'))  2 points

print(solve('x', (('x', '/', 'b'), '=', 'c')))
#  ('x', '=', ('c', '*', 'b'))  2 points

print(solve('y', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('y', '=', (('m', '*', 'x'), '+', 'b'))  2 points

print(solve('x', ('y', '=', (('m', '*', 'x'), '+', 'b'))))
# ('x', '=', (('y', '-', 'b'), '/', 'm'))  2 points

print(solve('a', (('b', '+', 'c'), '=', ('d', '*', (('a', '/', 'e'), '-', 'f')))))
# ('a', '=', (((('b', '+', 'c'), '/', 'd'), '+', 'f'), '*', 'e'))  5 points


