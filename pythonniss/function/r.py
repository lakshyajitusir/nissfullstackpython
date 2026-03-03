def reverse_string(s):
    if len(s) == 0:      # Base condition
        return s
    return reverse_string(s[1:]) + s[0]

name = "muna"
print(reverse_string(name))