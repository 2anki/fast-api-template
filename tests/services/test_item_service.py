import pytest
from app.models.items import Item
from app.services.item_service import calculate_total_price

def test_calculate_total_price_with_tax():
    """Test that calculate_total_price correctly adds tax when provided."""
    item = Item(name="Test Item", price=100.0, tax=20.0)
    total = calculate_total_price(item)
    assert total == 120.0

def test_calculate_total_price_without_tax():
    """Test that calculate_total_price works correctly when tax is not provided."""
    item = Item(name="Test Item", price=100.0)
    total = calculate_total_price(item)
    assert total == 100.0

def test_calculate_total_price_with_zero_tax():
    """Test that calculate_total_price works correctly when tax is zero."""
    item = Item(name="Test Item", price=100.0, tax=0.0)
    total = calculate_total_price(item)
    assert total == 100.0
