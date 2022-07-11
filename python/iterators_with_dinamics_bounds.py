import random

def finder(value: int, lower_bound: int, upper_bound: int) -> int:
    x = 0
    count = 0
    
    while x != value:
        trial = random.choice(range(lower_bound, upper_bound))
        count += 1
        print(f"upper_bound: {upper_bound} | lower_bound: {lower_bound}")
        
        if trial > value:
            upper_bound = trial
        elif trial < value:
            lower_bound = trial
        
        x = trial
        
        print(x)
    
    return count
  
