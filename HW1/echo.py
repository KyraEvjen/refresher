def echo(text: str, repetitions: int = 3) -> str:
    my_echo = ""
    while repetitions > 0:
        echo_piece = text[-repetitions:]
        repetitions = repetitions - 1
        my_echo = my_echo + echo_piece + "\n"
    return my_echo + "."


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
