def grocery_list(stock: dict[str, int], shop: dict[str, int]) -> list[str]:
    result: list[str] = []
    for item in shop:
        if item in stock:
            if shop[item] <= stock[item]:
                result.append(item)
    return result


stock: dict[str, int] = {"bread": 3, "chips": 1, "apples": 2}
shop: dict[str, int] = {"bread": 4, "apples": 2}
print(grocery_list(stock, shop))