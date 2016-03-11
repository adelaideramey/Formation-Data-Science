
# coding: utf-8

# In[17]:

#------------------------------------------#
#      LIST MANIPULATION IN PYTHON         #
#------------------------------------------#

#   A. match_ends

#   Given a list of strings,
#   return the count of the number of strings where :
#    - the string length is 2 or more 
#    - and the first and last chars of the string are the same.


def match_ends(words):
    
    longueur=len(words)
    output=[]
    test=[]

    for x in words:
        if len(x)>2 and x[0]==x[-1]:
        #output[len(output):] = [x]
            output.append(len(x))   
            output.append(x) 
    return output

liste=['assurance', 'ecurie','cheval','sacs','aa']
print liste
test=match_ends(liste)
print test


# In[59]:

#   B. front_x

#   Given a list of strings, 
#   return a list with the strings in sorted order, except group all the strings that begin with 'x' first.
#   e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
#   Hint: this can be done by making 2 lists and sorting each of them before combining them.

test=[]
def front_x(words):
    
    output=[]
    temp1=[]
    temp2=[]
    
    for x in words:
        if x[0]=='x' :
            temp1.append(x)
        else :
            temp2.append(x)
    temp1=sorted(temp1)
    temp2=sorted(temp2)
    #temp1.sort(reverse=True) #ne trie pas dans l'ordre alphabétique => checker l'option reverse
    #temp2.sort(reverse=True)
    output=temp1 +temp2
    del temp1
    del temp2
    return output

liste=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
print liste
test=front_x(liste)
print test


# In[74]:

#   C. sort_last

#   Given a list of non-empty tuples, 
#   return a list sorted in increasing order by the last element in each tuple.
#   e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
#   Hint: use a custom key= function to extract the last element form each tuple.

def last(t):
    return t[-1]
def sort_last(tuples):
    return sorted(tuples,key=last)

chaine=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
sort_last(chaine)


# In[55]:

#   D. remove_adjacent

#   Given a list of numbers, 
#   return a list where all adjacent == elements have been reduced to a single element, 
#   so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.

def remove_adjacent(nums):
    i=1
    while i < len(nums):    
        if nums[i] == nums[i-1]:
            nums.pop(i)
            i -= 1  
        else :
            i += 1
    return nums

liste=[1, 2, 2, 3]
print liste
test=remove_adjacent(liste)
print test


# In[86]:

#   E. linear_merge

#   Given two lists sorted in increasing order, 
#   create and return a merged list of all the elements in sorted order. 
#   You may modify the passed in lists. Ideally, the solution should work in "linear" time, making a single pass of both lists.


def linear_merge(list1, list2):
    output = []
    for x in list1:
        output.append(x)
    for y in list2:
        output.append(y)
    output.sort()
    return output

liste1=[1,3,5]
liste2=[6,2]
test=linear_merge(liste1, liste2)
print test


# In[85]:


liste1=[1,3,5]
liste2=[2,4,6]
test=liste1+liste2[1:]
print test
test2=liste1=[1,3,5]
liste2=[2,4,6]
test2=liste1+liste2[0:]
print test2


# In[82]:

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])
main()

