class BinaryText:

    def __init__(self):
        pass

    def convert_text_to_ascii(self, text):
        return [ord(c) for c in text]

    def get_bynary_based_on_ascii(self, ascii):
        return format(ascii, "08b")

    def get_table_order(self, text):
        lst_chars = list(text)
        lst_ascii = self.convert_text_to_ascii(text)
        for i in range(len(lst_chars)):
            print(
                f"Char: {lst_chars[i]} - ASCII: {lst_ascii[i]} - Binary: {self.get_bynary_based_on_ascii(lst_ascii[i])}"
            )
