class AbstractMelonOrder():
    
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""
        if self.species == "christmas melon":
            base_price = 7.5
        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    order_type = "domestic"
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    
    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""
        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    
    def __init__(self, species, qty):
        super().__init__(species, qty)
        tax = 0
        passed_inspection = False

    def mark_inspection(passed):
        if passed == True:
            self.passed_inspection = True

            


