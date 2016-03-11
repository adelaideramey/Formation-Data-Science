
# coding: utf-8

# In[7]:

#   A. donuts

#   Given an int count of a number of donuts, 
#   return a string of the form 'Number of donuts: ', 
#   where is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count.
#   So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'

count = input("Saisissez un nombre de donuts : ")
count = int(count)
    
def donuts():
    if count<10:
        return 'Number of donuts: ' +str(count)
    else:
        return 'Number of donuts: many'
    
donuts()


# In[8]:

#   B. both_ends

#   Given a string s, 
#   return a string made of the first 2 and the last 2 chars of the original string, 
#   so 'spring' yields 'spng'. However, if the string length is less than 2, return instead the empty string.


def both_ends(words):
    if len(words)>2:
        return words[:2]+words[-2:]
    else:
        return ''
    
test=('spring')
both_ends(test)


# In[10]:

#   C. fix_start

#   Given a string s, 
#   return a string where all occurences of its first char have been changed to '*', 
#   except do not change the first char itself.
#   e.g. 'babble' yields 'ba**le'
#   Assume that the string is length 1 or more. 
#   Hint: s.replace(stra, strb) returns a version of string s where all instances of stra have been replaced by strb.

def fix_start(s):
    return s[0] + s[1:].replace(s[0],'*')

test=fix_start('springs')
print test


# In[11]:

#  D. MixUp

#  Given strings a and b, 
#  return a single string with a and b separated by a space '<a> <b>', 
#  except swap the first 2 chars of each string.
#  e.g.'mix', pod' -> 'pox mid' 'dog', 'dinner' -> 'dig donner'
#  Assume a and b are length 2 or more.



def mix_up(a, b):
    return b[:2]+a[2:]+' '+a[:2]+b[2:]


test=mix_up('mix','pod')
print test


# In[13]:

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
#Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.


def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many') 

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
#We call the main function.


main()
#Donuts paramétrés en dynamique


# In[18]:

#   E. not_bad

#   Given a string, find the first appearance of the substring 'not' and 'bad'. 
#   If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'.
#   Return the resulting string.
#   So 'This dinner is not that bad!' yields: This dinner is good!

def not_bad(s):
    i = s.find('not')
    j = s.find('bad')
    if (j > i):
        return s[:i] + 'good' + s[(j+3):]
    return s
  
s=('This dinner is not that bad!')
not_bad(s)
 


# In[20]:

#   F. front_back

#   Consider dividing a string into two halves. 
#   If the length is even, the front and back halves are the same length. 
#   If the length is odd, we'll say that the extra char goes in the front half.
#   e.g. 'abcde', the front half is 'abc', the back half 'de'.
#   Given 2 strings, a and b, return a string of the form a-front + b-front + a-back + b-back

def front_back(a, b):
    i = int(len(a)/2+(len(a)%2))
    j = int(len(b)/2+(len(b)%2))
    return a[:i]+b[:j]+a[i:]+b[j:]
  
a=('mix')
b=('pod')
front_back(a,b)


# In[25]:



