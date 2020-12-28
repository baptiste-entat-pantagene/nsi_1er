class manager:
    def __init__(self):
        self._instance = []
    
    def new(self, newInstance):
        nextID = len(self._instance)
        self._instance.append(newInstance(nextID))
    
    def get_LastInstance_ID(self):
        return self._instance[len(self._instance) -1].get_ID()

    def get_LastInstance(self):
        return self._instance[len(self._instance) -1]
    
    def get_AllInstance(self):
        return self._instance
    
    def get_InstanceByID(self, ID:int):
        return self._instance[ID]


class instanceType1:
    def __init__(self, id:int = 0):
        self._id = id
    
    def get_ID(self):
        return(self._id)


manag = manager()

for i in range(0, 5):
    manag.new(instanceType1)

print(" instance ID==4->", manag.get_InstanceByID(4))



