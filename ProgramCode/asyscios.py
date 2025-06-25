
from pandas.errors import InvalidIndexError
import  time
import asyncio as asyncio

async def Task1():
    try:
        for i in range(5):
            print("Task1")
            asyncio.sleep(1)
            print("Task1 finished")
    except:
        InvalidIndexError


async def Task2():
    try:
        for i in range(5):
               print("Task2")
               asyncio.sleep(1)
               print("Task2 finished")
    except:
        InvalidIndexError


async def main():
  cr1 =Task1()
  cr2=Task2()
  await asyncio.gather(cr1,cr2)
  print("Main method ")


if __name__ =='__main__':
    asyncio.run(main())

