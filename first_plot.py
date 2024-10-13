from matplotlib import pyplot as plt

years=(2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009)
salary=(60000,61000,62000,63000,64000,65000,66000,67000,68000,69000)

plt.plot(years,salary)
plt.xlabel('Years')
plt.ylabel('Salary')
plt.title('Salary Over Years')
plt.show()