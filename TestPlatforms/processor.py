from multiprocessing import Process, Value, Lock, Array
import os
import time


number = [12]

def func(ingress,result):
    for ValueIndexer,ingress in enumerate(number):
        result[ValueIndexer] = str(number)
    
    


if __name__ == "__main__":
    ProcessorNodesActive = []
    ProcessorNodePossible = os.cpu_count()
    result = Array('i',200)
    for k in range(ProcessorNodePossible):
        poolNode = Process(target = func, args = (number,result))
        ProcessorNodesActive.append(poolNode)
    for eachProcess in ProcessorNodesActive:
        eachProcess.start()
    for eachProcess in ProcessorNodesActive:
        eachProcess.join()
    for eachProcess in ProcessorNodesActive:
        eachProcess.close()

    print (result[:])