class PriceCalculator:
    IVA_RATE: float = 0.21

    @staticmethod
    def apply_iva(subtotal: float) -> float:
        rate = PriceCalculator.IVA_RATE
        return round(subtotal + subtotal * rate, 2)

    @staticmethod
    def apply_discount(subtotal: float, percent: float) -> float:
        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100.")
        return round(subtotal - subtotal * percent / 100, 2)

    @staticmethod
    def apply_coupon(subtotal: float, coupon: float) -> float:
        if coupon > subtotal:
            raise ValueError("The coupon amount cannot exceed the subtotal.")
        return round(subtotal - coupon, 2)

    @staticmethod
    def apply_shipping(subtotal: float, cost: float, threshold: float = 100) -> float:
        if cost <= 0:
            raise ValueError("Cost must be greater than 0.")
        if subtotal >= threshold:
            return subtotal
        return round(subtotal + cost, 2)