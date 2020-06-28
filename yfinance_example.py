# Import the yfinance. If you get module not found error the run !pip install yfinance from your Jupyter notebook
import yfinance as yf

# Get the data for the stock AAPL
data = yf.download('PFE','2019-06-20','2020-06-20')
print(data['\nDate']);
i = 0;
for row in data['Adj Close']:
    print(i)
    print(row);
    i = i + 1
# print(data['Adj Close']);

# Import the plotting library
import matplotlib.pyplot as plt
# %matplotlib inline

# Plot the close price of the AAPL
# data['Adj Close'].plot()
# plt.show()