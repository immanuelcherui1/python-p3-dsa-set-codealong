# class MySet:

#     def first_repeated_value(list):
#         for i in range(0, len(list)):
#             for j in range(i+1, len(list)):
#                 if list[i] == list[j]:
#                     return list[i]
#         return None
    
    
#     def first_repeated_value(list):
#         # create a Set to keep track of values we've seen
#         number_set = set()
#         # iterate over each element from the list
#         for i in range (0, len(list)):

#             # if we've already seen a value, we've found the duplicate!
#             if list[i] in number_set:
#                 return list[i]
#             # otherwise, add the value to our set
#             number_set.add(list[i])
#         # return None if we reach the end and haven't found our value
#         return None

# first_repeated_value([1,2,3,3,4,4])
# # => 3


class MySet:
    
    def __init__(self, list = []):
        self.dictionary = {}
        for value in list:
            self.dictionary[value] = True
            
    def has(self, value):
        return value in self.dictionary
    
    def add (self, value):
        self.dictionary[value] = True
        return self
    
    def delete (self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size (self):
        return len (self.dictionary)
    
    # def clear(self):
    #     list = []
        
    #     def __str__(self):
    #         return f"MySet: {{{', '.join(str(e) for e in self.elements)}}}"

        


set = MySet([1, 2, 3, 3])