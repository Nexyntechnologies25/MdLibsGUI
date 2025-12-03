import random
import tkinter as tk
from tkinter import ttk

adjectives = ["spooky", "wild", "chaotic", "messy", "tiny", "bright", "scary", "mysterious", "smelly", "funky", "pretty"]
nouns = ["dragon", "taco", "robot", "crowd", "grandma", "mother", "dog", "bunny", "hamster", "employee", "alien", "pickle", "eggplant", "tomatoes"]
verbs = ["danced", "sprayed", "exploded", "dreamt", "called", "screamed", "ran", "vanished", "sprinted", "attacked", "sang", "teleported"]
places = ["the moon", "the park", "Walmart", "the beach", "Puerto Rico", "your house", "Florida", "Fort Pierce", "Alpaccian Mountains"]

story_simple = [
    "One day, a {adj} {noun} {verb} near {place}.",
    "A {adj} {noun} suddenly {verb} while walking to {place}.",
]

story_chaos = [
    "Out of nowhere a {adj}, {adj2}, {adj3} {noun} {verb} into {place}, ruining everything!",
    "A {adj} {noun} {verb} so loudly in {place} that 3 people cried.",
]

story_expert = [
    "{name} traveled to {place} with a {adj} {object_item}, but suddenly {enemy} {verb}.",
    "In {place}, {name} found a {adj} {object_item} that changed everything when {enemy} {verb}.",
]
names = ["Maxxine", "Mariah", "Ksi", "Selena", "Nick", "Gaston", "Jose", "Mario", "Jason", "Queen", "Bethany"]
objects = ["sword", "timepiece", "backpack", "spray bottle", "crystal", "walkie talkie", "Aloe plant", "plate", "robotic component", "animal"]
enemies = ["smurfette", "a goblin", "the illuminati", "a ghost", "artificial intelligence", "their evil twin", "their prettier twin", "the grinch", "Auntie Debby", "the grinch"]

def generate_story(mode):
    adj = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    adj3 = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    place = random.choice(places)
    name = random.choice(names)
    object_item = random.choice(objects)
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
        object_item = object_item,
        enemy = enemy,
    )

    return story

window = tk.Tk()
window.title("Mad Libs Generator")
window.geometry("600x500")
window.configure(bg = "#f2e9ff")

title_label = tk.Label(
    window,
    text = "Random Mad Libs Generator",
    font = ("Arial", 18, "bold"),
    bg = "#f2e9ff",
    fg = "#4c0080"
)
title_label.pack(pady = 10)

mode_box = ttk.Combobox(window, values = ["Simple", "Chaotic", "Expert"])
mode_box.set("Simple")
mode_box.pack(pady = 5)

story_box = tk.Text(
    window,
    height = 10,
    width = 60,
    wrap = "word",
    font = ("Arial", 12),
    bg = "#ffffff",
    fg = "#000000",
    relief = "solid",
    borderwidth = 2
)
story_box.pack(pady = 15)

def on_generate():
    mode = mode_box.get()
    story = generate_story(mode)
    story_box.delete(1.0, tk.END)
    story_box.insert(tk.END, story)

generate_button = tk.Button(
    window,
    text = "Generate Story",
    command = on_generate,
    font = ("Arial", 14, "bold"),
    bg = "#b366ff",
    fg = "white",
    activebackground = "#9933ff",
    activeforeground = "white",
    pady = 5
)
generate_button.pack(pady = 5)

quit_button = tk.Button(
    window,
    text = "Quit",
    command = window.destroy,
    font = ("Arial", 12),
    bg = "#ffb3b3",
    fg = "black",
    activebackground = "#ff9999",
    padx = 10,
    pady = 5
)
quit_button.pack(pady = 10)
window.mainloop()