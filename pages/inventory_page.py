from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def add_product_to_cart(self, product_name: str):
        product_card = self.page.locator(
            '[data-test="inventory-item"]'
        ).filter(has_text=product_name)

        product_card.get_by_role(
            "button",
            name="Add to cart"
        ).click()