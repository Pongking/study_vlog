import multiprocessing

#store a global variable
result=multiprocessing.Value("i",0)

def calcule_age(numbers,result):
    tmp_sum=sum(numbers)
    with result.get_lock():
        result.value+=tmp_sum

if __name__=='__main__':
    numbers=[1,2,3,4,5,6,7,8,9,10]
    numbers1=numbers[:len(numbers)//2]
    numbers2=numbers[len(numbers)//2:]
    processing1=multiprocessing.Process(target=calcule_age,args=(numbers1,result))
    processing2=multiprocessing.Process(target=calcule_age,name=(numbers2,result))
    processing1.start()
    processing2.start()
    processing1.join()
    processing2.join()
    print(result.value)