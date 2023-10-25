# Import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Store pop as a numpy array: np_pop


# Double np_pop


gdp_cap = [1,2,3,4,5,8]
life_exp =['1y','4y','5y','8y','10y','6y']

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()