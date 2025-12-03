import random
import tkinter as tk
from tkinter import ttk

adjectives = ["spooky", "wild", "chaotic", "messy", "crazy", "tiny", "bright", "mysterious", "rebelious", "smelly", "scary", "funky", "pretty", "furry", "glowing", "ferocious"]
nouns = ["dragon", "taco", "eggplant", "granny", "mother", "dog", "bunny", "robot", "hamster", "eagle", "crackhead", "celebrity", "papparazi", "employee", "manager", "bus driver"]
verbs = ["danced", "sprayed", "screamed", "cried", "fired", "exploded", "vanished", "talked", "sprinted", "sang", "layed", "collapsed", "flew"]
places = ["Walmart", "a mansion", "a cruise ship", "the lake", "the pool", "your house", "Publix", "a drive-through", "the beach", "Florida", "Alpaccian Mountains", "the mall", "the movies"]

story_simple = [
    "One day, a {adj} {noun} {verb} near {place}.",
    "A {adj} {noun} suddenly {verb} while walking to {place}."
]
story_chaos = [
    "Out of nowhere, a {adj}, {adj2}, {adj3} {noun} {verb} into {place}!",
    "A {adj} {noun} {verb} so loudly in {place} that 3 people sued!"
]
story_expert = [
    "{name} traveled to {place} with a {adj} {object}, but suddenly {enemy} {verb}.",
    "In {place}, {name} found a {adj} {object} that changed everything when {enemy} {verb}."
]
names = ["Ksi", "Bethany", "Jason", "Ricky", "Max", "Eliza", "Dessi", "Jose", "Tate", "Rebecca", "Tiffany", "Mario", "Elli"]
objects = ["backpack", "carrot", "robotic component", "stick", "umbrella", "Starbucks cup", "tablet", "shoes", "lunchbox"]
enemies = ["Smurfette", "their evil twin", "their prettier twin", "the demon", "the shark", "a crackhead", "nuns"]

def generate_story(mode):
    adj = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    adj3 = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    place = random.choice(places)
    name = random.choice(names)
    object = random.choice(objects)
    enemy = random.choice(enemies)

    if mode == "Simple":
        template = random.choice(story_simple)
    elif mode == "Chaotic":
        template = random.choice(story_chaos)
    else:
        template = random.choice(story_expert)
    
    story = template.format(
        adj = adj,
        adj2 = adj2,
        adj3 = adj3,
        noun = noun,
        verb = verb,
        place = place,
        name = name,
        object = object,
        enemy = enemy
    )
    return story
window = tk.Tk()
window.title("Mad Libs - Modern Edition")
window.geometry("650x550")
window.configure(bg = "#f6f2ff")

title_label = tk.Label(
    window,
    text = "â··Modern Mad Libs Generator â··",
    font = ("Helvetica", 20, "bold"),
    bg = "#f6f2ff",
    fg = "#5a189a"
)
title_label.pack(pady = 20)

mode_box = ttk.Combobox(
    window,
    values = ["Simple", "Chaotic", "Expert"],
    font = ("Helvetica", 12),
    state = "readonly"
)
mode_box.set("Simple")
mode_box.pack(pady = 10)

story_frame = tk.Frame(
    window,
    bg = "white",
    highlightthickness = 2,
    highlightbackground = "#bda7ff",
    padyx = 20,
    pady = 20
)
story_frame.pack(pady =20)

story_box = tk.Text(
    story_frame,
    height = 10,
    width = 60,
    wrap = "word",
    font = ("Helvetica", 12),
    bg = "white",
    fg = "#2d2d2d",
    relief = "flat"
)
story_box.pack()

def generate():
    mode = mode_box.get()
    story_box.delete(1.0, tk.END)
    story_box.insert(tk.END, generate_story(mode))

generate_button = tk.Button(
    window,
    text = "Generate Story",
    font = ("Helvetica", 14, "bold"),
    bg = "#7b2cbf",
    fg = "white",
    activebackground = "#5a189a",
    activeforeground = "white",
    padyx = 15,
    pady = 8,
    relief = "raised",
    bd = 3,
    command = generate
)
generate_button.pack(pady =5)

quit_button = tk.Button(
    window,
    text = "Quit",
    font = ("Helvetica", 12),
    bg = "#ffccd5",
    fg = "black",
    activebackground = "#ffb3c1",
    padyx = 12,
    pady = 6,
    command = window.destroy
)
quit_button.pack(pady = 10)

window.mainloop()