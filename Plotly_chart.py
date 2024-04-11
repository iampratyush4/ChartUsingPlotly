import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

def calculate_heikin_ashi(df):
    ha_df = pd.DataFrame(index=df.index)
    ha_df['Close'] = (df['Open'] + df['High'] + df['Low'] + df['Close']) / 4
    ha_df['Open'] = ((df['Open'].shift(1) + df['Close'].shift(1)) / 2).fillna(df['Open'])
    ha_df['High'] = ha_df[['Open', 'Close']].join(df['High']).max(axis=1)
    ha_df['Low'] = ha_df[['Open', 'Close']].join(df['Low']).min(axis=1)
    return ha_df

# Download stock data
ticker = 'AAPL'
data = yf.download(ticker, start='2023-01-01', end='2023-04-01')

# Calculate Heikin Ashi
ha_data = calculate_heikin_ashi(data)

# Plot with Plotly
fig = go.Figure(data=[go.Candlestick(x=ha_data.index,
                open=ha_data['Open'],
                high=ha_data['High'],
                low=ha_data['Low'],
                close=ha_data['Close'],
                increasing_line_color='green', decreasing_line_color='red')])

fig.update_layout(title=f'Heikin Ashi Chart for {ticker}', xaxis_title='Date', yaxis_title='Price', xaxis_rangeslider_visible=False)
fig.show()
