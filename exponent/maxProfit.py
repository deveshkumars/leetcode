from typing import Dict, List, Optional

def max_profit(prices: Dict[str, int]) -> Optional[List[str]]:
    if len(prices) == 0:
        return None
    price_min = float('inf')
    min_city = ""
    price_max = 0
    max_city = ""
    for key in prices:
        if prices[key] < price_min:
            min_city = key
            price_min = prices[key]
        if prices[key] > price_max:
            max_city = key
            price_max = prices[key]
        
    if price_min == price_max or min_city == "" or max_city == "":
        return None
    return [min_city, max_city]
    
    
# debug your code below
prices = {'London': 72, 'New York': 70, 'Tokyo': 67, 'Miami': 62}
print(max_profit(prices))
