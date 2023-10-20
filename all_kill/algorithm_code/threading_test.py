import threading

result=0
result_lock=threading.Lock()

def calculate_sum(numbers):
    global result
    partial_sum=sum(numbers)
    print(partial_sum)
    with result_lock:
        result+=partial_sum

if __name__ =='__main__':
    numbers=[1,2,3,4,5,6,7,8,9,10]
    split_num1=numbers[:len(numbers)//2]
    split_num2=numbers[len(numbers)//2:]
    thread1=threading.Thread(target=calculate_sum,args=(split_num1,))
    thread2=threading.Thread(target=calculate_sum,args=(split_num2,))
    thread1.start()    
    thread2.start()
    thread1.join()    
    thread2.join()
    print(result)    
