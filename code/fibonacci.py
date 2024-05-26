N = int(input("Please Enter Your Desired Number Of Fibonacci Digits To Print:"))


def desired_number(N: int):
    bag_of_many_numbers = [0, 1]
    for i in range(2, N):
        # print(i)
        # print(bag_of_many_numbers)
        sum_of_numbers = bag_of_many_numbers[-1] + bag_of_many_numbers[-2]
        bag_of_many_numbers.append(sum_of_numbers)
    # print ("The Sum Of Your Desired Number Of", N, "Fibonacci Digits Is", sum_of_numbers)
    return float(bag_of_many_numbers[-1])


my_desired_number = desired_number(N)
print(my_desired_number)
