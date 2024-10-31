import asyncio
from binance_stream import binance_streamer
from uniswap_stream import uniswap_streamer
from arbitrage import arbitrage_detector
from utils import log_arbitrage_opportunity, log_price_data

async def main():
    price_cex = None
    price_dex = None

    async def get_cex_price():
        nonlocal price_cex
        async for price in binance_streamer("ethusdt"):  # Пара AAVE/USDT
            price_cex = float(price)
            log_price_data("CEX (Binance)", price_cex)  # Запись данных о цене
            if price_dex:
                result = await arbitrage_detector(price_cex, price_dex)
                if result:
                    log_arbitrage_opportunity(result)

    async def get_dex_price():
        nonlocal price_dex
        async for price in uniswap_streamer():
            price_dex = float(price)
            log_price_data("DEX (Uniswap)", price_dex)  # Запись данных о цене
            if price_cex:
                result = await arbitrage_detector(price_cex, price_dex)
                if result:
                    log_arbitrage_opportunity(result)

    try:
        await asyncio.gather(get_cex_price(), get_dex_price())
    except asyncio.CancelledError:
        print("Программа завершена.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем.")
