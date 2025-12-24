import matplotlib.pyplot as plt
# Data
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
sales = [10, 30, 20, 50, 40, 60, 90]
days_num = [1, 2, 3, 4, 5, 6, 7]

# Bar Graph
plt.bar(days, sales)
plt.title("My First Graph")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

# Pie Chart
plt.pie(sales, labels=days, autopct='%1.1f%%')
plt.title("Sales Distribution Over the Week")
plt.show()

# Scatter Plot
plt.scatter(days_num, sales)
plt.title("Sales Data")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.xticks(days_num, ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
plt.show()

plt.show()
