from app.models.items import Item


def calculate_total_price(item: Item) -> float:
    """
    Calculate the total price of an item including tax.

    Args:
        item: The item object containing price and optional tax

    Returns:
        float: The total price including tax
    """
    return item.price + (item.tax or 0)
