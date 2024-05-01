import sys, random, time

sys.stdout = open('output.txt', 'w')

t1 = time.perf_counter()
for i in range(10000000):

    #get random ascii value
    ascii_val = random.randint(97, 122)
    #convert ascii value to character
    char = chr(ascii_val)
    #print the character
    print(char, end='')

t2 = time.perf_counter()
sys.stdout = sys.__stdout__
print("Time taken: {:.5f} seconds".format(t2 - t1))