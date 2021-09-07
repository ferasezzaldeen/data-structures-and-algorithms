from left_joint import *

def test_happy_end():
  data1=HashTable()
  data1.add('one','hello')

  data2=HashTable()
  data2.add('one','world')
  assert left_join(data1,data2)==[['one', 'hello', 'world']]


def test_right_is_empty():
  data1=HashTable()
  data1.add('one','hello')
  data2=HashTable()
  data2.add('warth','jordan')
  assert left_join(data1,data2)==[['one', 'hello', None]]

def test_left_is_empty():
  data1=HashTable()
  data2=HashTable()
  data2.add('warth','jordan')
  assert left_join(data1,data2)==[]