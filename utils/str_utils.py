class StrUtils:
    @staticmethod
    def string_to_float(value: str) -> float:
        return float(value[1:].replace(',', ''))
