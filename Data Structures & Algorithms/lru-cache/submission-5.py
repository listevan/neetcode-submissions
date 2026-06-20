class ListNode:
        def __init__(self, p, n, k, v):
            self.p = p
            self.n = n
            self.k = k
            self.v = v

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.l = None
        

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        ln = self.d[key]
        
        if self.l != ln:
            # print("getting")
            ln.p.n = ln.n
            if ln.n:
                ln.n.p = ln.p

            if ln != self.l.p:
                ln.p = self.l.p

            ln.n = self.l
            self.l.p = ln

            self.l = ln
        # print("getting", key, ln.k, ln.v)
        return ln.v  

    def put(self, key: int, value: int) -> None:
        # print(key, value)
        

        if key not in self.d:
            ln = ListNode(None, None, key, value)
            self.d[key] = ln
        else:
            ln = self.d[key]
            ln.v = value

        if self.l != ln:
            if ln.p:
                ln.p.n = ln.n
                if ln.n:
                    ln.n.p = ln.p


            if self.l:
                if ln != self.l.p:
                    ln.p = self.l.p
            else:
                ln.p = ln
            
            ln.n = self.l
            if self.l:
                self.l.p = ln
                
            self.l = ln
        
        if len(self.d) > self.capacity:
            tbr = self.l.p
            self.l.p = self.l.p.p
            self.l.p.n = None
            # print("deleting", tbr.k, tbr.v)
            del self.d[tbr.k]
        
        # print("*"*50)
        # head = self.l
        # while head:
        #     print(head.k, head.v, head.p.k)
        #     head = head.n
        # print("*"*50)
