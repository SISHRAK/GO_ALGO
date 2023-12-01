from moexalgo import Ticker

# выбираем акции Сбера
sber = Ticker('SBER')

# получим дневные свечи с 2020 года
sber.candles(date='2020-01-01', till_date='2023-11-01', period='D').head()
