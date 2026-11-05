print("Hello from mycode!")

person = "mike"

def say_hi(name: str) -> None:
    print(f"Hi {name}!")

def add( number: list[float]) -> float:
    return sum(number)

#test add
def test_add():
    # test 1 
    numbers = [1, 2, 3, 4, 5]
    result = add(numbers)
    assert result == 15, f"Expected 15 but got {result}"

    # test 2
    numbers = [0]
    result = add(numbers)
    assert result == 0, f"Expected 0 but got {result}"

# run your tests
if __name__ == "_main_": 
    print("Running tests...")
    test_add()

    # when you import this module, the tests will not run because the condition is not met. 
    # But if you click run on this file, the tests will run because the condition is met.
    # it blocks the tests from running when the module is imported, but allows them to run when the module is executed directly.