#!/usr/bin/python
# -*- coding: utf-8 -*-
import turtle


def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """

    count = 0
    while n != 1:
        #print('Iteration ' + str(count))
        #print('Value of n: ' + str(n))
        if n % 2 == 0:  # n is even
            n = n // 2
        else: # n is odd
            n = n * 3 + 1
        count += 1
    #print('This is iteration ' + str(count))
    #print('And the value of n should be 1, it is ' + str(n))
    return count  # the last print is 1

def turtleGraph(n):
  print("inside function, n is ", n)
  turt1 = turtle.Turtle()
  turt1.speed(1)
  turt1.up()
  turt2 = turtle.Turtle()
  wn = turtle.Screen()
  wn.setworldcoordinates(0, 0, 10, 10)
  max_so_far = 0 
  for i in range(1, n +1):
    result = seq3np1(i)
    if max_so_far <= result: 
      max_so_far = result
      wn.setworldcoordinates(0, 0, n + 10, max_so_far + 10)
      turt1.clear()
      turt1.goto(0, max_so_far)
      turt1.write(f"Maximum so far: starting value{i} _iteratios {max_so_far}")
      turt1.up()
    turt2.goto(i, seq3np1(i))
  wn.exitonclick
       

def main():
  start = int(input("Please enter a positive number:"))
  if start < 1:
    return 
  for i in range(1,start+1):
    print("This is i", i)
    iteration_count = seq3np1(i)
    print("Final interation count", iteration_count)

  turtleGraph(start)
  
main()
