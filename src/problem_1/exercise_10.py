import warnings


class Product:
    """
    Represents a product with a name, price, and stock information.

    :param name: The name of the product.
    :param price: The price of the product.
    :param stock: The available stock of the product.
    """

    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock


class ShoppingCart:
    """
    Represents a shopping cart that allows adding and removing products.

    :ivar items_on_cart: A list of tuples containing the products and their quantities in the cart.
    """

    def __init__(self):
        self.items_on_cart = {}

    def add_item(self, product: Product, quantity: int):
        """
        Adds a specified quantity of a product to the cart.

        :param product: The product to add to the cart.
        :param quantity: The quantity of the product to add.
        """
        if product.stock >= quantity:
            self.items_on_cart[product] = quantity
            product.stock -= quantity
            print(f"{quantity} {product.name}(s) added to the cart.")
        else:
            warnings.warn(f"Insufficient stock for {product.name}.")

    def remove_item(self, product: Product, quantity: int):
        """
        Removes a specified quantity of a product from the cart.

        :param product: The product to remove from the cart.
        :param quantity: The quantity of the product to remove.
        """
        item_quantity = self.items_on_cart.get(product)
        if item_quantity:
            if quantity >= item_quantity:
                del self.items_on_cart[product]
                product.stock += item_quantity
                print(f"All {product.name}(s) removed from the cart.")
            else:
                self.items_on_cart[product] -= quantity
                product.stock += quantity
                print(f"{quantity} {product.name}(s) removed from the cart.")
        else:
            raise ValueError(f"{product.name} not found in the cart.")

    def display_cart(self):
        """
        Displays the contents of the shopping cart and the total cost.
        """
        if not self.items_on_cart:
            print("Your cart is empty.")
        else:
            print("Your shopping cart:")
            total_cost = sum(
                product.price * quantity for product, quantity in self.items_on_cart.items()
            )
            for product, quantity in self.items_on_cart.items():
                print(
                    f"{product.name}: {quantity} x ${product.price} = ${product.price * quantity}"
                )
            print(f"Total cost: ${total_cost}")
