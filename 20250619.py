def main():
    print("Hello, World!")
    
if __name__ == "__main__":
    main()


def test_main():
    assert main() == "Hello, World!"


print(main())

test_main()


def test_1():
    assert 1 == 1

def test_2():
    assert 2 == 2

def test_3():
    assert 3 == 3

def test_4():