"""
PROBLEM:

A client comes into our store and needs to buy exactly two gifts. 
The friends who will receive them are very dear to him, 
so he wants to spend as much as possible of the X dollars he has set aside for these gifts. 
Say you have a list of prices for all products on our store and the gifts can be any of these products 
(regardless of gender, size, utility, etc). 
Please write an algorithm that determines the maximum amount he can spend out of the X dollars he has.
You can simply describe the solution in pseudo-code. 
Also, more valuable than the answer is the thought process, 
so please feel free to describe any ideas you have or wrong leads you discard, and why.
"""

"""
Return a list of values of which sum doens't over max_value
"""   
def getValues(values, max_value):
    # compair value and max_value, return True if successful.
    def compair(value):
        if value <= compair.max_value:
            compair.max_value -= value
            return True
        else:
            return False

    compair.max_value = max_value
    return filter(compair, sorted(values, None, reverse=True))

values = [13, 15, 18, 20, 26, 29, 31, 37, 39, 43, 47]
max_value = 115
results = getValues(values, max_value)
print(results, sum(results))
