from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "PKWMKE7NQOPR1Q8J95MO"
API_SECRET = "BgUWLtED1d1sFFbrg0qWplf28HrJ8RCSnob6tsGb"
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

# Allow to inherit from Strategy class
class MLTrader(Strategy):
    
    def initialize(self, symbol:str="SPY"):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None
    
    def on_trading_iteration(self):
        if self.last_trade == None:
            order = self.create_order(
                symbol=self.symbol,
                qty=10,
                side="buy",
                type="market"
            )
            self.submit_order(order)
            self.last_trade = "buy"
    
start_date = datetime(2023,12,15)
end_date = datetime(2023,12,31)
broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker=broker, 
                    parameters={"symbol": "SPY"})
strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={"symbol": "SPY"}
)
