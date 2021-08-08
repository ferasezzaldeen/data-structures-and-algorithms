import pytest 
from stack_and_queue import Queue, Stack, Node, StackEmptyException


def test_tests():

  assert 1 == 1


@pytest.fixture
def data():
  new_stack = Stack()

  return {'stack':new_stack}


#Can successfully push onto a stack
def test_stack_pushing_one_element(data):
  data['stack'].push(1)
  actual = data['stack'].top.value
  expected = 1
  assert actual == expected


#Can successfully push multiple values onto a stack
def test_stack_push_lots_of_values():
  test =Stack()
  test.push(1)
  test.push(2)
  test.push(3)
  assert test.top.value==3

#Can successfully pop off the stack
def test_stack_pop_one_element(data):
    data['stack'].push(1)
    data['stack'].push(2)
    actual = data['stack'].pop()
    expected = 2
    assert expected == actual

#Can successfully empty a stack after multiple pops
def test_empty_after_pops():
  test =Stack()
  test.push(1)
  test.push(2)
  test.push(3)
  test.pop()
  test.pop()
  test.pop()
  assert test.top==None

#Can successfully peek the next item on the stack
def test_stack_peak():
  test =Stack()
  test.push(1)
  test.push(2)
  test.push(3)
  assert test.peek()==3


#Can successfully instantiate an empty stack
def test_stack_is_empty():
  stack = Stack()
  assert stack.is_empty()


#Calling pop or peek on empty stack raises exception
def test_peek_empty_stack_raises_exception():
  check_stack = Stack()
  with pytest.raises(Exception, match ="empty stack" ):
    check_stack.peek()



#Can successfully enqueue into a queue
def test_enqueue_from_queue():
  test=Queue()
  test.enqueue(1)
  assert test.front.value==1

#Can successfully enqueue multiple values into a queue
def test_enqueue_more_then_one_queue():
  test=Queue()
  test.enqueue(1)
  test.enqueue(2)
  assert test.front.value==1 and test.rear.value==2

#Can successfully dequeue out of a queue the expected value
def test_dequee_more_then_one_queue():
  test=Queue()
  test.enqueue(1)
  test.enqueue(2)
  test.enqueue(3)
  test.dequeue()

  assert test.front.value==2


#Can successfully peek into a queue, seeing the expected value
def test_peek_queue():
  test=Queue()
  test.enqueue(1)
  test.enqueue(2)
  test.enqueue(3)
  
  assert test.peek()==1

#Can successfully empty a queue after multiple dequeues
def test_peek_queue():
  test=Queue()
  test.enqueue(1)
  test.enqueue(2)
  test.enqueue(3)
  test.dequeue()
  test.dequeue()
  test.dequeue()
  assert test.rear==None and test.front==None


#Can successfully instantiate an empty queue
def test_empty_queue():
  test=Queue()
  assert test.is_empty()

#Calling dequeue or peek on empty queue raises exception
def test_dequeue_from_empty_queue():
  test=Queue()
  with pytest.raises(Exception, match ="empty queue" ):
    test.dequeue()