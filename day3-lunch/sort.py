#!/usr/bin/env python

import random
r = random.randint(1, 100)

#print r
#nums = []

#for i in xrange(5):
#    r = random.randint(1, 100)
#    print "the %dth number is %d" % (i, r)
#    nums.append(r)
    
#print nums

#nums.sort()

nums = range(0, 100, 10)
print nums

key = 10 #random.randint(1, 100)

#for i, v in enumerate( nums ): is same thing as the next for statement
    
#for i in xrange(len(nums)):
 #   v = nums[i]
  #  print "scanning the %dth number is %d" % (i, v)
   # if (v == key):
    #    print "found it at position %d" % (i)
 
 
 
 ### binary search ###    
hi = len(nums)
lo = 0
#key_lost = True

#while key_lost:
while lo <= hi:
    mid = (hi + lo) / 2
    middle = nums[mid]
    print "checking in the range [%d, %d] mid[%d]=%d" % (lo, hi, mid, middle)

# this is one method:    
#    if key == middle:
#        print "found at position %d" % (mid)
#        key_lost = False
#    elif key < middle:
#        hi = mid - 1
#    elif key > middle:
#        lo = mid + 1

#this is another method:
    if (middle == key):
        print "found %d at position %d" % (middle, mid)
        break
    elif (key > middle):
        lo = mid + 1
    elif (key < middle):
        hi = mid - 1
    
        
            
            
            
            
            

         
        
    
 

    