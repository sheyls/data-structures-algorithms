import random

class RandomizedSet(object):

    def __init__(self):
        self.random_set = {}
        self.random_list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.random_set:
            return False

        self.random_list.append(val)
        self.random_set[val] = len(self.random_list) - 1
        return True        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.random_set:
            return False
        
        index = self.random_set[val]
        last_value = self.random_list[-1]
        self.random_list[index], self.random_list[-1] = last_value, self.random_list[index]
        self.random_set[last_value] = index
        self.random_list.pop()
        self.random_set.pop(val)
        return True


    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.random_list)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()