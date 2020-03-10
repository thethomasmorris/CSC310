"""
Thomas Morris
Make Up Assignment
October 31st, 2019
"""
def hanoi(n, rod1, rod2, rod3):
    if(n == 1):
        print("Move disk 1 from rod ",rod1," to rod ",rod3)
        return
    hanoi(n-1, rod1, rod2, rod3)
    print("Move disk ",n,"from rod ",rod1,"to rod",rod3)
    hanoi(n-1, rod2, rod3, rod1)

if __name__ == "__main__":
    hanoi(2, "A", "B", "C")
    
