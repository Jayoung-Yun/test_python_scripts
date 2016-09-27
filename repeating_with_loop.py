word = 'lead'
print word[0]
print word[1]
print word[2]
print word[3]


print '========================'
word = 'oxygen'
for char in word:
  print char  # space is necessar!

length = 0
for vowel in 'aeiou' :
  length = length +1
  print ('  In loop : There are'), length, ('vowels')

print ('There are'), length, ('vowels')

print '========================'
letter = 'z'
for letter in 'abc':
  print letter
print ('after the loop, letter is'), letter

print len('aeiou')

print '====[ From 1 to N ]===='
for i in range(1, 10, 2) : 
  print (i)

for i in range(3, 10, 3) : print (i)

print "====[ Computing Powers With Loops ]===="
print 5**3
exp = 1
for i in range(0,3) :
   exp = exp * 5
   print i, exp
print exp

print "====[ Reverse a String ]===="
rev_word = ''
org_word = 'Newton'
for char in org_word:
  #rev_word = rev_word + char
  rev_word = char + rev_word
  print char 
  print rev_word
  
