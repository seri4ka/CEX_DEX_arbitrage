import asyncio

# Ловим арбитраж, сравнивая цены
async def arbitrage_detector(price_cex, price_dex, threshold=0.001):
    """
    Проверка арбитража между ценами CEX и DEX.
    
    Parameters:
        price_cex (float): Цена ETH/USDT на CEX (Binance).
        price_dex (float): Цена ETH/USDT на DEX (Uniswap).
        threshold (float): Минимальная разница в цене для открытия арбитража.
        
    Returns:
        str: Сообщение об арбитражной возможности.
    """
    # Рассчитываем разницу в цене
    difference = abs(price_cex - price_dex) / min(price_cex, price_dex)

    # Если разница превышает порог, сигнализируем об арбитраже
    if difference > threshold:
        if price_cex > price_dex:
            return f"Арбитражная возможность: Купить на DEX ({price_dex:.2f}) и продать на CEX ({price_cex:.2f})"
        else:
            return f"Арбитражная возможность: Купить на CEX ({price_cex:.2f}) и продать на DEX ({price_dex:.2f})"
    return None