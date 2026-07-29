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

    

