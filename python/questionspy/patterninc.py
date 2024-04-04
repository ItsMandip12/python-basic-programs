arr=["a","b","c","d"]
for i in range(arr[0],arr[3]):
    for j in range(arr[0],arr[i]):
        print(arr[i],end="")
    print("\n",end="")

    # *
    # **
    # ***
    # ****
    # *****

    # ******
    # ****
    # ***
    # **
    # *