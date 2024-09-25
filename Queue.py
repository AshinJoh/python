Q = []

def enqueue(item):
    Q.append(item)

def dequeue():
    if Q:
        return Q.pop(0)
    else:
        return "Queue is empty"

def display():
    return Q

def front():
    if Q:
        return Q[0]
    else:
        return "Queue is empty"

def rear():
    if Q:
        return Q[-1]
    else:
        return "Queue is empty"

# Example usage
enqueue(10)
enqueue(20)
print(display())   # Output: [10, 20]
print(front())     # Output: 10
print(rear())      # Output: 20
