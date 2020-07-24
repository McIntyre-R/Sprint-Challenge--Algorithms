#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I believe this one ends up being O(n) because the amount of operations needed to be performed will always equal the input size given n*n*n and the time it'll take for a+n*n to catch up to that


b) I'm not super sure on this one, so for this I believe it'll grow exponentially as the end sum will always be n*(n//2) which I think will result in it being O(n2)


c) This one should be linear given the function should only run as big as the input size performing one recursive call for each item in the input, and ends when its gone through each item once which would be O(n)

## Exercise II



# I believe this function comes out to be O(log N) with a binary search. Which is moderately better than O(n)
# Create a function that performs a binary search through the given floors

def egg(n):

# Midpoint to begin search

  mid = n//2
  
# Search while within bounds of given building

  while not mid <= 0 and not mid > n:

# Check if egg breaks when thrown

    if throw_egg(mid) == 'Broken':

# If Egg does break, check if floor below also breaks

      if throw_egg(mid-1) == 'Not Broken':

# If true floor is f

        return f = mid

# Otherwise f is a floor lower than ours, so start at a middle point below current mid, and repeat

      mid = mid//2

# If egg isn't initially broken check if floor above breaks

    elif throw_egg(mid) == 'Not Broken':
      if throw_egg(mid+1) == 'Broken':
        return f = mid
      mid += mid//2

# Helper function to emulate throwing the egg

def throw_egg(floor):
  target = 20
  if floor < target:
    return 'Not Broken'
  else:
    return 'Broken'
