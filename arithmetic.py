def add(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

def subtract(nums):
    diff = nums[0]
    for num in nums[1:]:
        diff -= num
    return diff


def multiply(nums):
    product = 1
    for num in nums:
        product *= num
    return product


def divide(nums):
    result = nums[0]
    for num in nums[1:]:
        result /= num
    return result


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return float(num1) ** float(num2)  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
