my_str = 'sobit learning python from Kshitiz Sir'

str_freq = {}
str_freq_arr = []

for s in my_str:
    if s not in str_freq:
        str_freq[s] = 1
    else:
        str_freq[s] = str_freq[s] + 1

    for key in str_freq:
        val = str_freq[key]
    str_freq_arr.append(val)
print(str_freq)

