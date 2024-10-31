import asyncio
import websockets
import json

async def binance_streamer(symbol: str = "ethusdt"):
    print(f"Запуск стриминга Binance для пары {symbol}")
    url = f"wss://stream.binance.com:9443/ws/{symbol}@ticker"
    try:
        async with websockets.connect(url) as ws:
            while True:
                data = await ws.recv()
                ticker_data = json.loads(data)
                price = ticker_data['c']  # Текущая цена закрытия
                print(f"Цена на Binance: {price}")  # Выводим цену для проверки
                yield price
                await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Стриминг Binance остановлен.")
