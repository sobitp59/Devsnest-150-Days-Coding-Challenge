def solve(n, nums):
    stack = []
    NGE = []

    for i in range(2*n):
        while len(stack) > 0 and stack[-1] < nums[i%n]:
            stack.pop()
        if i < n:
            if len(stack) > 0:
                # NGE.append(stack[-1])    
                NGE[i] = stack[-1]
            else:
                # NGE.append(-1)
                NGE[i] = -1
        stack.append(nums[i%n])

    return stack, NGE
    
print(solve(4,[1,3,2,4]))