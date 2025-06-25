import multiprocessing

def squaring(num):
    '''
    this the use for  square '''
    print(f"Square of hte number{num*num}")

def cubing(num):
    '''this is the cube of the numebr'''
    print(f"Cubes of the  number {num*num*num}")


if __name__ =='__main__':
    p1  = multiprocessing.Process(target= squaring, args=(10,))
    p2 = multiprocessing.Process(target= cubing,args=(10,))

    p1.start()
    p2.start()


    p1.join()
    p2.join()

    print('!done')



