# ## Intro to Asynchronous Programming 
# - In Synchronous Programming, everything runs/executes synchronously. If there are  four functions defined:-A,B,C,D. Then first A will run and the next function will not start untill A has finisehd executing.
# - Now Asynchronous programming changes the way it works here by executing other functions also even if A or the first function hasnt been finished.So you can execute B,C,D even while A hasnt finished executing yet.This increases the efficeincy of our program
# - `asyncio` is a Python library used for writing concurrent code using the async/await syntax. It allows you to run multiple I/O-bound operations concurrently, such as reading from files, making network requests, or interacting with databases, without blocking the program's execution
# - Eventloop is at heart of asyncio .It is responsible for scheduling and executing asynchronous tasks
# - Coroutines: A coroutine is a special type of function defined using async def. You can use the await keyword inside coroutines to pause their execution until another asynchronous task finishes. 
# - Task: To run coroutines in eventloop ,u need to wrap them in task object .You can schedule coroutines to run in the event loop by creating tasks.
# - A Future is an object that represents the result of an operation that is not yet complete. It can be used to check if a task has finished

# Basic Example of asyncio:

import asyncio

async def my_coroutine():
  print("start")
  await asyncio.sleep(2) # This is non-blocking and allows other tasks to run
  print("end")


asyncio.run(my_coroutine())

# In this case, await asyncio.sleep(1) allows the event loop to do other work while the current coroutine is paused. If there are any other tasks running in the event loop (like other coroutines), they could execute while asyncio.sleep(1) is waiting.


# async def my_coroutine():
 # You define an asynchronous function (or coroutine) named my_coroutine.
 # This function contains await calls, meaning it can pause its execution and let other tasks run in the meantime.
 # In this case, it will pause for 2 second with await asyncio.sleep(2).

# The await keyword pauses the execution of my_coroutine without blocking the whole program.
# asyncio.sleep(2) simulates a non-blocking delay of 2 second. While this coroutine is "sleeping", the event loop can continue running other coroutines or tasks (if they were present).

# asyncio.run(my_coroutine()):
  # this is an entry point for running your asynchronous code
  # asyncio.run() runs the coroutine passed to it (in this case, my_coroutine()) and manages the event loop for you.
  # It sets up the event loop, runs the coroutine, and ensures that the loop is closed properly once the coroutine completes.

# Execution of code:-
# print("Start") is called and immediately printed to the console.
# as await is encountered it will wait till the proceeding work is completed,so here it is sleep(2) so it will wait for 2 sec meanwhile the event loop can run other coroutines if present
# After 1 second, print("End") is executed and printed to the console.
