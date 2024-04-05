import os


def nice_print(loaded_value, expected_value):
    print(f"expected_value: {expected_value}")
    print(f"loaded_value: {loaded_value}")
    print(f"expected_unicode_value == loaded_unicode_value: {expected_value == loaded_value}")
    print(f"expected bytes: <{bytes(expected_value, 'utf-8')}> loaded bytes: <{bytes(loaded_value, 'utf-8')}>")


def main():
    expected_unicode_value = "/🐜/⚙️/🐳"
    loaded_unicode_value = os.environ.get("UNICODE_VALUE")
    additional_unicode_value = os.environ.get("ADDITIONAL_UNICODE_VALUE")

    print("comparison with unicode value loaded from .env file")
    nice_print(loaded_unicode_value, expected_unicode_value)
    print("*" * 80)
    print("comparison with unicode value loaded from environment config")
    nice_print(additional_unicode_value, expected_unicode_value)

    expected_not_unicode_value = "/this/is/plain/text"
    loaded_not_unicode_value = os.environ.get("NOT_UNICODE_VALUE")
    print("*" * 80)
    print("comparison with not unicode value loaded from .env file")
    nice_print(loaded_not_unicode_value, expected_not_unicode_value)


if __name__ == "__main__":
    main()
