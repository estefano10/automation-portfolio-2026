class PriceCalculator:
    IVA_RATE = 0.21

    @staticmethod
    def apply_iva(subtotal):
        rate = PriceCalculator.IVA_RATE
        return round(subtotal + subtotal * rate, 2)

    @staticmethod
    def apply_discount(subtotal, percent):
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100.")
        return round(subtotal - subtotal * percent / 100, 2)

    @staticmethod
    def apply_coupon(subtotal, coupon):
        if coupon > subtotal:
            raise ValueError("The coupon amount cannot exceed the subtotal.")
        return round(subtotal - coupon, 2)

    @staticmethod
    def apply_shipping(subtotal, cost, threshold=100):
        if cost < 0:
            raise ValueError("Cost must be greater than 0.")
        if subtotal >= threshold:
            return subtotal
        return round(subtotal + cost, 2)



