import sympy as sp
import matplotlib.pyplot as plt

def gradient_descent(starting_point, learning_rate, num_iterations):
    x_value = starting_point  
    x = sp.symbols('x')  
    f_x = x**2 + 6*x + 8  
    gradient = sp.diff(f_x, x)  
    f_values = [] 
    
    for i in range(num_iterations):
        gradient_value = gradient.subs(x, x_value)
        x_value = x_value - learning_rate * gradient_value
        f_x_value = f_x.subs(x, x_value)
        
        # Lưu giá trị của f(x) 
        f_values.append(f_x_value)
    
    return f_values

learning_rates = [0.001, 0.01, 0.1, 1.0]
num_iterations = int(input("Nhap so lan lap :"))  
starting_point = float(input("Nhap diem khoi dau :"))  
# Vẽ đồ thị của f(x) theo số bước lặp
plt.figure(figsize=(10, 6))

for lr in learning_rates:
    f_values = gradient_descent(starting_point, lr, num_iterations)
    plt.plot(range(num_iterations), f_values, label=f'learning_rate = {lr}')

plt.xlabel('Số bước lặp')
plt.ylabel('Giá trị của f(x)')
plt.title('Sự thay đổi của f(x) theo số bước lặp với các learning_rate khác nhau')
plt.legend()
plt.grid(True)
plt.show()