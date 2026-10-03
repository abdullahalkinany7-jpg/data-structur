class family:
    def __init__(self,name,ne=None):
        self.name=name
        self.ne=ne
def list_family(ele):
    while ele!=None:
        print(ele.name)
        ele=ele.ne

def add(list,ele):
    new=family(ele)
    if list==None:
        list=new
    else:
        while list.ne!=None:
            list=list.ne
        list.ne=new
def get_ele(first,index):
    p=first
    if index<0:
        print("erore")
        return
    else :
        i=0
        while i<index and p!=None:
            p=p.ne
            i+=1
        print(p.name)
def del_ele(first,ele):
    p=first
    q=None
    while p!=None and p.name!=ele:
        q=p
        p=p.ne
    if p==None:
        print("the ele is not eixst")
    else:
        if p==first:
            first=first.ne
        else:
            q.ne=p.ne
    return first
f1=family("ali")
f2=family("ahmed")
f3=family("jasm")
first=f1
f1.ne=f2
f2.ne=f3
first=del_ele(first,"ahmed")
list_family(first)
