import pytest

from src.problem_1.exercise_10 import Product


def test_add_item(setup_shopping_cart):
    """
    Test adding items to the shopping cart.
    GIVEN a shopping cart and products,
    WHEN adding items to the cart,
    THEN the cart should contain the added items with correct quantities.
    """
    cart, apple, banana, _, _ = setup_shopping_cart
    cart.add_item(apple, 3)
    cart.add_item(banana, 2)
    assert len(cart.items_on_cart) == 2
    assert apple in cart.items_on_cart
    assert cart.items_on_cart[apple] == 3
    assert banana in cart.items_on_cart
    assert cart.items_on_cart[banana] == 2


def test_add_item_insufficient_stock(setup_shopping_cart):
    """
    Test adding items with insufficient stock to the shopping cart.
    GIVEN a shopping cart and a product with insufficient stock,
    WHEN attempting to add the product to the cart,
    THEN a message indicating insufficient stock should be displayed.
    """
    cart, apple, _, _, _ = setup_shopping_cart
    with pytest.warns(match="Insufficient stock for Apple"):
        cart.add_item(apple, 20)


def test_remove_item(setup_shopping_cart):
    """
    Test removing items from the shopping cart.
    GIVEN a shopping cart with items,
    WHEN removing items from the cart,
    THEN the cart should contain the remaining items with correct quantities.
    """
    cart, apple, _, _, _ = setup_shopping_cart
    cart.add_item(apple, 3)
    cart.remove_item(apple, 2)
    assert len(cart.items_on_cart) == 1
    assert cart.items_on_cart[apple] == 1


def test_remove_item_all(setup_shopping_cart):
    """
    Test removing all items of a product from the shopping cart.
    GIVEN a shopping cart with items,
    WHEN removing all items of a product from the cart,
    THEN the cart should not contain that product anymore.
    """
    cart, apple, _, _, _ = setup_shopping_cart
    cart.add_item(apple, 3)
    cart.remove_item(apple, 3)
    assert len(cart.items_on_cart) == 0


def test_remove_item_not_in_cart(setup_shopping_cart):
    """
    Test removing a product not in the shopping cart.
    GIVEN a shopping cart without a product,
    WHEN attempting to remove the product from the cart,
    THEN a message indicating the product is not found should be displayed.
    """
    cart, _, _, _, _ = setup_shopping_cart
    with pytest.raises(ValueError, match="Nonexistent not found in the cart."):
        cart.remove_item(Product("Nonexistent", 1.0, 10), 1)


def test_display_cart_empty(setup_shopping_cart, capsys):
    """
    Test displaying an empty shopping cart.
    GIVEN an empty shopping cart,
    WHEN displaying the cart,
    THEN a message indicating the cart is empty should be displayed.
    """
    cart, _, _, _, _ = setup_shopping_cart
    cart.display_cart()
    captured = capsys.readouterr()
    assert "Your cart is empty." in captured.out


def test_display_cart(setup_shopping_cart, capsys):
    """
    Test displaying a non-empty shopping cart.
    GIVEN a shopping cart with items,
    WHEN displaying the cart,
    THEN the cart contents and total cost should be displayed correctly.
    """
    cart, apple, banana, orange, pineapple = setup_shopping_cart
    cart.add_item(apple, 3)
    cart.add_item(banana, 2)
    cart.add_item(orange, 1)
    cart.add_item(pineapple, 1)
    cart.display_cart()
    captured = capsys.readouterr()
    assert "Apple: 3 x $1.99 = $5.97" in captured.out
    assert "Banana: 2 x $0.99 = $1.98" in captured.out
    assert "Orange: 1 x $1.49 = $1.49" in captured.out
    assert "Pineapple: 1 x $2.99 = $2.99" in captured.out
    assert "Total cost: $12.43" in captured.out
