class MathOperations:
    def add(self, a, b=None, c=None):
        if b is not None and c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a
# Example Usage
math_obj = MathOperations()
result1 = math_obj.add(5)
result2 = math_obj.add(5, 10)
result3 = math_obj.add(5, 10, 15)
# Output
print(result1)
print(result2)
print(result3)