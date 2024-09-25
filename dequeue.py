from collections import deque

people = ['Mario', 'Luigi', 'Toad']
queue = deque(people)

queue.append('Bowser')
print(queue[0])

queue.popleft()
print(queue)

queue.appendleft('Daisy')
print(queue)

queue.rotate(-2)
print(queue)

queue.extend(['Yoshi', 'Sonic'])
print(queue)

queue.reverse()
print(queue)
