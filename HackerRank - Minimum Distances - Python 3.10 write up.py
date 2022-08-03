##    https://www.hackerrank.com/challenges/minimum-distances/problem
##
##    The distance between two array values is the number of indices between
##    them. Given a, find the minimum distance between any pair of equal
##    elements in the array. If no such value exists, return -1.

##### ##### ##### #####

#   O(n)
#   n is the number of elements in a

#   Idea:
#       The distance between any two equal elements is the number of
#       indices between them.  Therefore we need to know the index of the
#       current element and the index of its previous appearance.
#       With this in mind we can iterate through the given array
#       and keep track of an element and the index it appears at in a dictionary:

#           key:value => element:index

#       If an index already exists for the current element, calculate the distance,
#       then replace the old index with the current index.  Check if the distance
#       is smaller than the smallest distance found.  If it is, save it.

#   Algo:
#       1. Initiate index table(dictionary) for storing an element with the
#           index of its previous appearance => O(1)
#       2. Initiate variable to store the smallest distance found => O(1)
#       3. For each element in a => O(|a|)
#               if the element has previously appeared: => O(1)
#                   calculate the distance => O(1)
#                   check if shorter than current shortest, store if true => O(1)
#                   replace old index with current index => O(1)
#               else:
#                   create entry in dictionary (element:index) => O(1)
#       4. Return shortest distance => O(1)

#   Note:
#       As always, (try, except) logic leads to very clean code when creating and
#       manipulating dictionaries.

def minimumDistances(a):
    
    index_table = dict()
    minimum_distance = len(a) + 1
    
    for index in range(len(a)):
        
        try:
            
            current_distance = index - index_table[a[index]]
            
            if current_distance < minimum_distance:
                
                minimum_distance = current_distance
                
            index_table[a[index]] = index
            
        except:
            
            index_table[a[index]] = index
    
    if minimum_distance == len(a) + 1:
        
        return -1
    
    else:
        
        return minimum_distance
