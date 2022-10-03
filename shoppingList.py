class shopping(list):
    
    isles = [['apples', 'oranges'], ['beef', 'pork'], ['carrots', 'cabbage']]

    def __init__(self, arr):
        super(shopping, self).__init__(arr)
        self.__d = {}
        for i in range(0, len(self)):
            if arr[i] in self.__d.keys():
                self.__d[self[i]] += 1
            else:
                self.__d[self[i]] = 1
    
    def __add__(self, value):
        self.append(value)
        if value in self.__d.keys():
            self.__d[value] += 1
        else:
            self.__d[value] = 1
    
    def __repr__(self):
        rtn = []
        for k in self.__d.keys():
            isle = -1
            for i in range(0, len(self.isles)):
                if k in self.isles[i]:
                    isle = i
            rtn.append([k , self.__d[k], isle])
            #make into sentence and then return as array of sentences like an actual shopping list
            rtn.append(str(self.__d[k]) + str(k) + 'on isle' + str(isle))
        return str(rtn)

#s = shopping(['apples', 'oranges', 'beef', 'carrots'])
#print(s)

#s + 'apples'
#print(s)