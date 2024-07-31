class StringProcessor:
    @staticmethod
    def reverse_and_uppercase(s: str) -> str:
        return s[::-1].upper()

    @staticmethod
    def remove_vowels(s: str) -> str:
        vowels = "aeiouAEIOU"
        return "".join([char for char in s if char not in vowels])

    @staticmethod
    def count_words(s: str) -> int:
        return len(s.split())
