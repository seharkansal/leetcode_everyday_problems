# for i in range(5):
#     for j in range(5):
#         print('*',end="")
#     print()
k=5
for i in range(5):
    for j in range(0,k):
        print(end=" ")
    k-=1

    for j in range(0,2*i+1):
        print('*',end="")

    # for j in range(4,0,-1):
    #     print(end=" ")

    print()
        