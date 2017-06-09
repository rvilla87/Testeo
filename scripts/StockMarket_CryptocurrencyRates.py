import time, subprocess
from datetime import datetime
from rtstock.stock import Stock
from moneywagon import get_current_price

# Use telegram-send command-line tool in order to send a Telegram message
def telegram_alert(message):
    # telegram-send app must be in PATH and first run with --configure-channel
    # More info in https://github.com/rahiel/telegram-send
    subprocess.call('telegram-send --config trader.conf "' + message + '"', shell=True)
    print(message)


# Define custom stock market alerts
TSLA_low = 355  # Tesla
TSLA_high = 385
MSFT_low = 60   # Microsoft
MSFT_high = 80
NVDA_low = 145  # NVIDIA
NVDA_high = 175
WESAS_low = 14  # WES.AS
WESAS_high = 16

btc_low = 2400  # Bitcoin
btc_high = 2800
eth_low = 225   # Ethereum
eth_high = 275
etc_low = 10    # Ethereum Classic
etc_high = 25
zec_low = 225   # Zcash
zec_high = 275


print("Monitoring stock market and cryptocurrency rates...")
while True:
    # Print actual timestamp
    print(datetime.now().strftime("%d/%m/%y %H:%M:%S"))

    # Get actual stock market prices
    TSLA = float(Stock('TSLA').get_latest_price()[0]["LastTradePriceOnly"])  # Tesla
    MSFT = float(Stock('MSFT').get_latest_price()[0]["LastTradePriceOnly"])  # Microsoft
    NVDA = float(Stock('NVDA').get_latest_price()[0]["LastTradePriceOnly"])  # NVIDIA
    WESAS = float(Stock('WES.AS').get_latest_price()[0]["LastTradePriceOnly"])  # WES.AS

    btc = get_current_price('btc', 'eur')  # Bitcoin
    eth = get_current_price('eth', 'eur')  # Ethereum
    etc = get_current_price('etc', 'eur')  # Ethereum Classic
    zec = get_current_price('zec', 'eur')  # Zcash


    # Trigger telegram's alert (if any)
    if TSLA < TSLA_low: telegram_alert("Tesla low price: " + str(TSLA))
    if TSLA > TSLA_high: telegram_alert("Tesla high price: " + str(TSLA))
    if MSFT < MSFT_low: telegram_alert("Microsoft low price: " + str(MSFT))
    if MSFT > MSFT_high: telegram_alert("Microsoft high price: " + str(MSFT))
    if NVDA < NVDA_low: telegram_alert("NVIDIA low price: " + str(NVDA))
    if NVDA > NVDA_high: telegram_alert("NVIDIA high price: " + str(NVDA))
    if WESAS < WESAS_low: telegram_alert("WES.AS low price: " + str(WESAS))
    if WESAS > WESAS_high: telegram_alert("WES.AS high price: " + str(WESAS))

    if btc < btc_low: telegram_alert("Bitcoin low price: " + str(btc))
    if btc > btc_high: telegram_alert("Bitcoin high price: " + str(btc))
    if eth < eth_low: telegram_alert("Ethereum low price: " + str(eth))
    if eth > eth_high: telegram_alert("Ethereum high price: " + str(eth))
    if etc < etc_low: telegram_alert("Ethereum Classic low price: " + str(etc))
    if etc > etc_high: telegram_alert("Ethereum Classic high price: " + str(etc))
    if zec < zec_low: telegram_alert("Zcash low price: " + str(zec))
    if zec > zec_high: telegram_alert("Zcash high price: " + str(zec))

    # We will monitor the rates every 5 minutes
    time.sleep(300)
