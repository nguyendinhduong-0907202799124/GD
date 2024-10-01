import sympy as sp

x = sp.symbols('x')
f_x = x**2 + 6*x + 8
f_prime = sp.diff(f_x, x)
print(f"Dao ham cua f(x) là: {f_prime}")
print("Cuc tieu cua f(x) la:",-6/2)

def gradient_descent(starting_point, learning_rate, num_iterations):
    x = starting_point
    for i in range(num_iterations):
        gradient = 2*x + 6
        x= x - learning_rate * gradient
        print(f"Iteration {i+1}: x = {x}, f(x) = {x**2 + 6*x + 8}")

starting_point = float(input("Nhap diem khoi dau cho thuat toan : "))
learning_rate = float(input("Nhap toc do hoc : "))
num_iterations = int(input("Nhap so lan lap : "))
gradient_descent(starting_point, learning_rate, num_iterations)