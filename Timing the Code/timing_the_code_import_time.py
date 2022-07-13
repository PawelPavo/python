import time

def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

def func_two(n):
    return list(map(str,range(n)))

print(func_two(10))

# Timinng the code - "import time"

# Function 1
# CURRENT TIME BEFORE CODE
start_time=time.time()

# RUN CODE
result=func_one(1000000)

# CURRENT TIME AFTER CODE
end_time=time.time()

# ELAPSED TIME
elapsed_time=end_time - start_time
print(elapsed_time)



# Function 2
# CURRENT TIME BEFORE CODE
start_time=time.time()

# RUN CODE
result=func_two(1000000)

# CURRENT TIME AFTER CODE
end_time=time.time()

# ELAPSED TIME
elapsed_time=end_time - start_time
print(elapsed_time)

