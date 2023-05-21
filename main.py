from contextlib import contextmanager


@contextmanager
def generic(card_type, sender_name, rec_arg):
    card_file = open(card_type, "r")
    order = open(f"{sender_name}_generic.txt", "w")
    try:
        order.write(f"Dear {rec_arg}, \n")
        order.write(card_file.read())
        order.write(f"\nSincerely, {sender_name} \n")
        yield order
    finally:
        card_file.close()
        order.close()


with generic("thankyou_card.txt", "Mwenda", "Amanda") as file:
    print("Card Generated!")

with open("Mwenda_generic.txt", "r") as first_order:
    print(first_order.read())


class personalized:
    def __init__(self, sender_name, receiver_name):
        self.sender_name = sender_name
        self.receiver_name = receiver_name
        self.file = open(f"{sender_name}_personalized.txt", "w")

    def __enter__(self):
        self.file.write(f"Dear {self.receiver_name}, \n \n")
        return self.file

    def __exit__(self, *exc):
        self.file.write(f"\n \n Sincerely, \n {self.sender_name}")
        self.file.close()


with personalized("John", "Michael") as card:
    card.write(
        "I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always."
    )

    with generic("happy_bday.txt", "Josiah", "Remy") as card, personalized(
        "Josiah", "Esther"
    ) as card2:
        card2.write(
            "Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!"
        )

# checkout if it's working
with open("Josiah_personalized.txt", "r") as first_order:
    print(first_order.read())
