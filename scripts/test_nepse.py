from nepsepy import NepseClient

with NepseClient() as client:
    status= client.market_status()
    gainers= client.top_gainers()
    prices= client.today_price(page= 1, size= 20)

    print(status["isOpen"])
    print(gainers[:3])
    print(prices["content"][:3]) 