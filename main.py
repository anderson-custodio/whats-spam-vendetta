import time
import pyautogui as pg
import webbrowser as web
import argparse
from unidecode import unidecode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("phone", help="Phone number", type=str)
    parser.add_argument("input_x", help="Input message x coordinate", type=int)
    parser.add_argument(
        "button_x", help="Send message button x coordinate", type=int)
    parser.add_argument(
        "y", help="Input or send message y coordinate", type=int)
    parser.add_argument(
        "message_file", help="Text file containing the messages to send", type=str)

    args = parser.parse_args()

    web.open(f"https://web.whatsapp.com/send?phone={args.phone}")

    time.sleep(8)

    data = open(args.message_file, "r")

    try:
        for msg in data:
            click(args.input_x, args.y) # <--- Click on the message input field
            m = unidecode(msg.rstrip())
            pg.write(m) # <--- Write the message
            click(args.button_x, args.y) # <--- Click on the send message button
            time.sleep(5) # <--- Change it to a lower number if you want to send messages faster
            print(m)
    finally:
        data.close()


def click(x, y):
    pg.move(x, y)
    pg.click(x, y)


if __name__ == "__main__":
    main()
