

#When we have an array with four elements in it (a,b,c,d). We want to find the maximum value in array



#First code

# largest = a
# if largest < b:
#     largest = b
# if largest < c:
#     largest = c
# if largest < d:
#     largest = d
# return largest





#Second code
# if a > b:
#     if a > c:
#         if a > d:
#             return a
#         else:
#             return d
#     else:
#         if c > d:
#             return c
#         else:
#             return d
# else:
#     if b > c:
#         if b > d:
#             return b
#         else:
#             return d
#     else:
#         if c > d:
#             return c
#         else:
#             return d 






# For humans the first code is more easier to read than second but, both have same level complexity for a computer to execute,but if we check the space, the first code needs more space in our computer, because of the temporary variable the variable need more space, and the second code does not include the variable and does not need much space as first