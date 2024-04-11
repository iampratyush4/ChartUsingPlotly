import plotly.graph_objects as go
import yfinance as yf

# Download stock data
ticker = 'AAPL'
data = yf.download(ticker, start='2023-01-01', end='2023-04-01')

# Create a simple candlestick chart
fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

fig.update_layout(title=f'{ticker} Stock Price', xaxis_rangeslider_visible=False)
fig.show()
