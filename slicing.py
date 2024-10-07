piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
tuple_keys = ("A", "B", "C", "D", "E", "F","G")

"""position 1 to 3, 2 items will be in it"""
print(piano_keys[1:3])
"""position 2 to the end"""
print(piano_keys[2:])
"""beginning to position 5"""
print(piano_keys[:5])
"""third number is step size, every second number in range here"""
print(piano_keys[1:6:2])
"""every second item of the entire list"""
print(piano_keys[::2])
"""every second item from top to position 5"""
print(piano_keys[:5:2])
"""reverse the sequence, only works when the first 2 numbers are empty"""
print(piano_keys[::-1])
"""similar to above"""
print(piano_keys[::-2])
"""you know"""
print(piano_keys[1::1])

"""everything works the same with tuples"""