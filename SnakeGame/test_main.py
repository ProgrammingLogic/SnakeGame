import main

def test_hello_world():
    assert main.__name__ == "__main__"
    assert main.print("Hello world!") == None

if __name__ == "__main__":
    test_hello_world()