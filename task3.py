class BracketChecker:
    MATCHING = {')': '(', '}': '{', ']': '['}
    OPENING = '({['
    CLOSING = ')}]'

    def __init__(self, expression: str):
        self.expression = expression

    def is_balanced(self) -> bool:
        stack = []
        for char in self.expression:
            if char in self.OPENING:
                stack.append(char)
            elif char in self.CLOSING:
                if not stack or stack.pop() != self.MATCHING[char]:
                    return False
        return not stack


if __name__ == "__main__":
    test_data = [
        '( ) { { [ ] ( ) ( ) { } } }',
        '( ( ( )',
        '( 1 + 2 ) * { 3 - [ 4 / ( 5 + 6 ) ] }',
        '( ){[ 1 ]( 1 + 3 )( ){ }}:',
        '( 23 ( 2 - 3);:',
        '( 11 }:'
    ]

    for test_expression in test_data:
        checker = BracketChecker(test_expression)
        result = checker.is_balanced()
        print(f"{test_expression}: {result}")