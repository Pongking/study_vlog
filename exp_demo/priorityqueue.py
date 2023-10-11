class  PriorityQueue:
    def __init__(self):
        self.heap=[]
        #基于堆的优先队列
    def _heapify_up(self,index):
        '''
        在新加入元素时，保持堆的性质
        '''
        parent_index=(index-1)//2
        while index>0 and self.heap[index][0]<self.heap[parent_index][0]:
            self.heap[index],self.heap[parent_index]=self.heap[parent_index],self.heap[index]
            index=parent_index
            parent_index=(index-1)//2

    def _heapify_down(self,index):
        '''
        在弹出堆顶元素时，维持堆的性质
        '''
        left_child_index=2*index+1
        right_child_index=2*index+2
        smallest=index
        if left_child_index<len(self.heap) and self.heap[left_child_index][0]<self.heap[smallest][0]:
            smallest=left_child_index
        if right_child_index<len(self.heap) and self.heap[right_child_index][0]<self.heap[smallest][0]:
            smallest=right_child_index
        if smallest!=index:
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            self._heapify_down(smallest)
        
        
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()[1]
        top_item=self.heap[0][1]
        self.heap[0]=self.heap.pop() #把最后的元素放到堆顶，并覆盖堆顶元素（即弹出堆顶元素），再进行重新堆化
        self._heapify_down(0)
        return top_item

    def push(self,item,priority):
        '''
        堆中存放的数据为(优先级,元素)
        '''
        self.heap.append((priority,item))
        self._heapify_up(len(self.heap)-1)

    def peek(self):
        if self.heap:
            return self.heap[0][1]
        return None
    def is_empty(self):
        return len(self.heap)==0    

pq=PriorityQueue()
pq.push("t1",3)
pq.push("t2",5)
pq.push("t3",8)
pq.push("t4",2)
pq.push("t5",1)
'''
优先级小的在前
t5
t4
t1
t2
t3
'''
print(pq.peek())
while not pq.is_empty():
    print(pq.pop())
