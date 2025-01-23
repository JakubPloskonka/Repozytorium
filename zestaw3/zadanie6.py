class UppercaseDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):

        result = self.func(*args, **kwargs)

        if isinstance(result, str):
            return result.upper()
        return result

@UppercaseDecorator
def print_message():
    return "hello, world!"

# Example
if __name__ == "__main__":
    print(print_message())
