from tkinter import *
import random
import time

#WORD

words = [
    "python", "flask", "database", "linux", "security",
    "network", "developer", "software", "keyboard",
    "internet", "algorithm", "application", "system",
    "server", "cloud", "github", "project", "student",
    "computer", "programming", "coding", "technology",
    "artificial", "intelligence", "cybersecurity"
]

start_time = None


#FUNCTIONS
def generate_text():
    return " ".join(random.choices(words, k=20))


def start_typing(event):
    global start_time

    if start_time is None:
        start_time = time.time()


def calculate_accuracy(original, typed):

    original_words = original.split()
    typed_words = typed.split()

    correct = 0

    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] == typed_words[i]:
            correct += 1

    if len(original_words) == 0:
        return 0

    accuracy = (correct / len(original_words)) * 100

    return round(accuracy)


def check_speed():

    global start_time

    if start_time is None:
        result_label.config(
            text="Start typing first!"
        )
        return

    original_text = sample_label.cget("text")

    typed_text = text_box.get("1.0", END).strip()

    end_time = time.time()

    elapsed_time = end_time - start_time

    minutes = elapsed_time / 60

    word_count = len(typed_text.split())

    if minutes > 0:
        wpm = round(word_count / minutes)
    else:
        wpm = 0

    accuracy = calculate_accuracy(
        original_text,
        typed_text
    )

    result_label.config(
        text=f"WPM: {wpm} | Accuracy: {accuracy}%"
    )


def new_test():

    global start_time

    start_time = None

    sample_label.config(
        text=generate_text()
    )

    text_box.delete("1.0", END)

    result_label.config(text="")


#UI

window = Tk()
window.title("Typing Speed Test")
window.geometry("800x550")
window.config(padx=20, pady=20)

title_label = Label(
    text="Typing Speed Test",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=10)

instructions = Label(
    text="Type the text below as fast and accurately as possible.",
    font=("Arial", 11)
)

instructions.pack()

sample_label = Label(
    text=generate_text(),
    wraplength=700,
    font=("Arial", 16),
    pady=20
)

sample_label.pack()

text_box = Text(
    width=80,
    height=8,
    font=("Arial", 12)
)

text_box.pack(pady=10)

text_box.bind("<Key>", start_typing)

check_button = Button(
    text="Check Speed",
    width=20,
    command=check_speed
)

check_button.pack(pady=10)

new_test_button = Button(
    text="New Test",
    width=20,
    command=new_test
)

new_test_button.pack()

result_label = Label(
    text="",
    font=("Arial", 16, "bold")
)

result_label.pack(pady=20)

window.mainloop()