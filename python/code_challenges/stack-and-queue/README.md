# Stacks and Queues
<!-- Short summary or background information -->
thay are a new tyoe of data structure,
A stack and queue is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

## Challenge
<!-- Description of the challenge -->
write some classes and methodes to deal with stacks and queues

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
my approch is descriped in my code: [code](./stack_and_queue.py)

## API
<!-- Description of each method publicly available to your Stack and Queue-->
For stack:
push: create a node containing the value and add it the top of the stack.
pop: will remove the the top of the stack and return its value.
peek: will return the value of the top without removing it.
is_empty : will return a boolean telling you if the stack is empty.

For queue:
enqueue: create a node containing the value and add it to the rear of our queue.
dequeue: will remove the the front of the queue and return its value.
peek: will return the value of the front without removing it.
is_empty : will return a boolean telling you if the queue is empty.
