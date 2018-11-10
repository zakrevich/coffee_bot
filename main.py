from extraction import get_name
from message import send_message


def main():
    name = get_name()
    send_message(name)


if __name__ == '__main__':
    main()
