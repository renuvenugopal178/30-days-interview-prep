from collections import deque

#stack

stack = []

stack.append("python")
stack.append("java")
stack.append("react")

print("stack:", stack)
print("popped item:", stack.pop())
print("stack after pop:", stack)

#queue

queue = deque()
queue.append("task 1")
queue.append("task 2")
queue.append("task 3")

print("queue:", list(queue))
print("removed from queue:",queue.popleft())
print("queue after removal:", list(queue))