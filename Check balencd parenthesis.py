#susovan
from IsMatching import isMAtching

def isBalanced(expr):
    stack=[]

    for x in expr:
        if x in ('(', '{', '['):
            stack.append(x)
        else:
            if not stack:
                return False
            elif isMAtching(stack[-1], x)==False:
                return False

            else:
                stack.pop()

    if stack:
        return False

    else:
        return True


print(isBalanced("[[[[[{{))}}}}}"))
