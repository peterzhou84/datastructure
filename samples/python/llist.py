#coding=utf-8

'''
链表的示例，来源周海君老师
'''
class lnode:
    def __init__(self,elem,nexte=None):
        self.elem=elem
        self.next=nexte
def inserhead(head,x): #在表头插入元素x
    p=lnode(x)
    p.next=head
    head=p
    return head
def printli(head):
    p=head
    # print(p.elem)
    a=[]
    while p!=None:
        #print(p.elem)
        a.append(p.elem)
        p=p.next
    print(a)
head=lnode(1)
b=[]
b.append(head.elem)
for i in range(2,9):
    head = inserhead(head,i)
    #p=lnode(i)#b.append(p.elem)    
    #p.next=head
    #head=p
printli(head)