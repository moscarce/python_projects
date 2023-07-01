for y in range(4):
    for x in range(1,10):
        print('#'*x) if y%3==0 else print('#'*(10-x))
    print(end='')