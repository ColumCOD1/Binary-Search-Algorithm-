# a function that takes a list and target parameter
# multiple variables : middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is done 
# conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0 
    end = len(list)
    steps = 0 
    
    while(start<=end):
        print("Step",steps, ":",(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle 
        if element < list[middle]:
            end = middle -1
        else:
            start = middle + 1

    return -1
            
lst = list(range(1,1001))
print(lst) 
target = 94

binary_search(lst, target) 
        