from web3 import Web3
import asyncio
import json
import time

async def uniswap_streamer():
    print("Запуск стриминга Uniswap V2 для пары ETH/USDT")
    
    # Загрузка ABI для Uniswap V2
    with open("ABI.json") as f:
        pool_abi = json.load(f)

    # Установка соединения с Ethereum через Infura
    rpc_url = "https://mainnet.infura.io/v3/79e9a671dff64ee5910b02058cfc0f2b"
    web3 = Web3(Web3.HTTPProvider(rpc_url))

    # Адрес пула ETH/USDT на Uniswap V2
    pool_address = "0x0d4a11d5EEaaC28EC3F61d100daF4d40471f1852"  # Адрес для Uniswap V2
    pool_contract = web3.eth.contract(address=pool_address, abi=pool_abi)

    try:
        while True:
            # Получаем резервы токенов
            reserves = pool_contract.functions.getReserves().call()
            reserve_eth = reserves[0]  # Резерв ETH
            reserve_usdt = reserves[1]  # Резерв USDT

            # Приведение резервов к одному масштабу
            reserve_eth_scaled = reserve_eth / (10 ** 18)  # ETH имеет 18 десятичных знаков
            reserve_usdt_scaled = reserve_usdt / (10 ** 6)  # USDT имеет 6 десятичных знаков

            # Вычисляем цену ETH/USDT
            price_eth_usdt = reserve_usdt_scaled / reserve_eth_scaled  # Цена в USD за 1 ETH

            # Выводим цену с временной меткой
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Цена на Uniswap: {price_eth_usdt}")
            yield price_eth_usdt
            await asyncio.sleep(1)  # Обновление каждую секунду
    except asyncio.CancelledError:
        print("Стриминг Uniswap остановлен.")
