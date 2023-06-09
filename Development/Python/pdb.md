# load pdb module
python -m pdb reallu_simple.py

# help
?

# list a file
l

# long list
ll

# next (step out the function)
n

# step into the function
s

# pretty print - use when you have variable that name is the same as pdb command, e .g. list
pp l

# setting a breakpoint to line 17
b 17

# setting a condition stop at a breakpoint
condition 1 b>=770

# setting a condition stop at a breakpoint, example 2
condition 2 (i % k + j % k) == 0

# disabling breakpoint 1
disable 1