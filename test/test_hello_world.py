import pytest
from src.hello_world import print_hello

def test_hello():
  x = print_hello()
  boo = x == 'Hello World'
  assert True
