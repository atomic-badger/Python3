#float For loops with break

# print statement describing loop 3
print("""
Now, let's try a new version of a 'for' loop.
    In this version, a condition will break the cycle early.\n

\tballoon = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9]
\tfor num in balloon:
    \t    print(num)
    \t    if num == 5.5:
            \tbreak
            
OUTPUT:
""")

# actual loop 3 - BREAK
balloon = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9]
for num in balloon:
    print(num)
    if num == 5.5:
        break
print("\nthis is the end of this for Loop using floats.\n")


    

