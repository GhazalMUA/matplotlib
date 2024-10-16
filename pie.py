labels = ['ghazal', 'bahrad', 'bardia']
num = [230, 100, 98] 
import matplotlib.pyplot as plt
plt.pie(num, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'yellow'])
plt.title('Voting Results: Club President', fontdict={'fontsize': 20})
plt.show()
