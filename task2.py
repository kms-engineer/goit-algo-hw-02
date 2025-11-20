from collections import deque


class PalindromeChecker:
    def __init__(self, text: str):
        self.original_text = text
        self.chars = deque(text.replace(' ', '').lower())

    def is_palindrome(self) -> bool:
        while len(self.chars) > 1:
            if self.chars.popleft() != self.chars.pop():
                return False
        return True


if __name__ == "__main__":
    test_data = ['tenet', 'python', 'madam', 'step on no pets', 'book', 'A man a plan a canal Panama']

    for test_string in test_data:
        checker = PalindromeChecker(test_string)
        result = checker.is_palindrome()
        print(f"String: '{test_string}' is palindrome: {result}")