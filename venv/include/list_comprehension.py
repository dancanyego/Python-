## Generating a list of squares

# squares =[1,4,9,25,36]
# Squares=[#expression #for_loop #condition]

squares = [i*i for i in range(0, 11)]
print(squares)

even_squares = [i*i for i in range(1, 11) if i%2==0]
print(even_squares)
odd_squares = [i*i for i in range(1, 11) if i%2!=0]
print(even_squares)