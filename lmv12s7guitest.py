# IMPORTS

import os, json, time, random
from normal_errors import *
from debug_errors import *
from banners import *
import performanceanalyzerv1 as performanceanalyzer

# --- TKINTER ARAYÜZÜ EKLENDİ ---
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# VARIABLES AND LISTS

global lst
lst = []
global history
history = []
global counter
counter = 1
global mode
mode = 0
global using
using = 0
global timer
timer = 0
global exited
exited = False
global v
v = "12snapshot7"
global V
V = "12 Snapshot 7"
global sv
sv = "12s7"

# --- FUN FACTS ---
fun_facts   = ["The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis'.",
            "Bananas are berries, strawberries aren't.",
            "Honey never spoils, archaeologists found jars full of honey in ancient Egyptian tombs.",
            "Ducks' quacks don't echo, nobody knows why.",
            "Sea water is salty because there is the sea in it.",
            "The average person eats 8 spiders a year is a complete fabrication, but don't sleep soundly. >:)",
            "When choosing the color of toothbrushes, it is actually difficult to decide among all the colors in the universe.",
            "A penguin is likely to be having fun while walking on land.",
            "Watermelons are the only fruit chosen by aliens, or maybe not.",
            "If a song repeats itself over and over, your brain memorizes it and you end up paying royalties to the song owner without even realizing it.",
            "If people actually lived 7.5 minutes longer, they would not be doing anything for the last 7.5 minutes.",
            "If a zombie stays in a room with you for 5 minutes, you don't forget to say 'Hi' to it.",
            "Actually, ostriches can fly but they are afraid.",
            "Watermelons just retain more water, but they're fun.",
            "If there is no world, you still exist, but perhaps on another planet. (Mysterious!)",
            "If you can read this, you are not blind.",
            "If you are reading this, you are not dead.",
            "If you are reading this, you are not a robot.",
            "If you are reading this, you are not a cat.",
            "If you are reading this, you are not a dog.",
            "If you are reading this, you are not a fish.",
            "You are you, me are me. ",
            "If you are reading this, you are not a tree.",
            "If you are reading this, you are not a rock.",
            "You can see this text in only List Manager, not in any other program.",
            "If you are reading this, you are not a human. >:)",
            "If you are reading this, you are not a computer. (can you?)",
            "If you are reading this, you are not a virus.",
            "You can't see this text in lower versions of List Manager.",
            "If you are reading this, you are not a bug."
            "You can do anything you want, but not in this program.",
            "1 + 1 = 2, but not in this program.",
            "Roses are red, violets are blue, if you are reading this, you are not a fool.",
            "If you are reading this, you are not a fool. >:)"
            ]

def fun_fact():
    return random.choice(fun_facts)

# --- TKINTER ARAYÜZÜ SINIFI ---

class ListManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"List Manager {V}")
        self.create_widgets()
        self.load_data()
        self.update_listbox()
        self.show_fun_fact()

    def create_widgets(self):
        self.listbox = tk.Listbox(self.root, width=50, height=15)
        self.listbox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.add_btn = tk.Button(self.root, text="Add", width=12, command=self.add_item)
        self.add_btn.grid(row=1, column=0, padx=5, pady=5)

        self.del_btn = tk.Button(self.root, text="Delete", width=12, command=self.delete_item)
        self.del_btn.grid(row=1, column=1, padx=5, pady=5)

        self.clean_btn = tk.Button(self.root, text="Clean", width=12, command=self.clean_list)
        self.clean_btn.grid(row=1, column=2, padx=5, pady=5)

        self.sort_btn = tk.Button(self.root, text="Sort", width=12, command=self.sort_list)
        self.sort_btn.grid(row=1, column=3, padx=5, pady=5)

        self.new_btn = tk.Button(self.root, text="New List", width=12, command=self.new_list)
        self.new_btn.grid(row=2, column=0, padx=5, pady=5)

        self.export_btn = tk.Button(self.root, text="Export", width=12, command=self.export_list)
        self.export_btn.grid(row=2, column=1, padx=5, pady=5)

        self.help_btn = tk.Button(self.root, text="Help", width=12, command=self.show_help)
        self.help_btn.grid(row=2, column=2, padx=5, pady=5)

        self.exit_btn = tk.Button(self.root, text="Exit", width=12, command=self.exit_program)
        self.exit_btn.grid(row=2, column=3, padx=5, pady=5)

        self.funfact_label = tk.Label(self.root, text="", fg="blue", wraplength=400, justify="left")
        self.funfact_label.grid(row=3, column=0, columnspan=4, pady=10)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for i, item in enumerate(lst, 1):
            self.listbox.insert(tk.END, f"{i}. {item}")

    def add_item(self):
        item = simpledialog.askstring("Add Item", "Enter item to add:")
        if item:
            if item in lst:
                messagebox.showwarning("Warning", "Item already exists!")
            else:
                lst.append(item)
                history.append("add")
                self.save_data()
                self.update_listbox()

    def delete_item(self):
        selection = self.listbox.curselection()
        if selection:
            idx = selection[0]
            item = lst[idx]
            lst.remove(item)
            history.append("delete")
            self.save_data()
            self.update_listbox()
        else:
            messagebox.showinfo("Info", "Select an item to delete.")

    def clean_list(self):
        if messagebox.askyesno("Clean List", "Are you sure you want to clean the list?"):
            lst.clear()
            history.append("clean")
            self.save_data()
            self.update_listbox()

    def sort_list(self):
        lst.sort()
        history.append("sort")
        self.save_data()
        self.update_listbox()

    def new_list(self):
        global counter
        if messagebox.askyesno("New List", "Create a new list? Current list will be saved."):
            self.save_data()
            counter += 1
            lst.clear()
            history.append("new")
            self.save_data()
            self.update_listbox()

    def export_list(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files","*.txt")])
        if filename:
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    for item in lst:
                        f.write(f"{item}\n")
                messagebox.showinfo("Export", f"List exported to {filename}")
                history.append("export")
            except Exception as e:
                messagebox.showerror("Error", f"Export failed: {e}")

    def show_help(self):
        help_text = (
            "Add: Add item to list\n"
            "Delete: Remove selected item\n"
            "Clean: Remove all items\n"
            "Sort: Sort items\n"
            "New List: Start a new list\n"
            "Export: Save list to a text file\n"
            "Help: Show this help\n"
            "Exit: Save and exit"
        )
        messagebox.showinfo("Help", help_text)

    def exit_program(self):
        self.save_data()
        self.root.destroy()

    def show_fun_fact(self):
        self.funfact_label.config(text="Fun Fact: " + fun_fact())

    def save_data(self):
        data = {
            "list": lst,
            "counter": counter,
            "history": history
        }
        with open("lmdata_gui.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_data(self):
        global lst, counter, history
        try:
            with open("lmdata_gui.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                lst[:] = data.get("list", [])
                counter = data.get("counter", 1)
                history[:] = data.get("history", [])
        except Exception:
            lst.clear()
            counter = 1
            history.clear()

# --- TKINTER ARAYÜZÜNÜ BAŞLATMAK İÇİN FONKSİYON ---

def start_gui():
    root = tk.Tk()
    app = ListManagerGUI(root)
    root.mainloop()

# PROGRAM

def main():
    # Kullanıcıya arayüz mü yoksa terminal mi sor
    try:
        import sys
        if hasattr(sys, 'ps1'):
            # Interactive shell'de çalışıyorsa GUI başlatma
            start_gui()
            return
        choice = input("Arayüz (GUI) ile başlatmak ister misiniz? (E/h): ").strip().lower()
        if choice in ("e", "evet", "y", "yes", ""):
            start_gui()
            return
    except Exception:
        pass
    ListManagerGUI.load_data()
    ListManagerGUI.save_data()
    
    global exited

    if mode == 0:
        print(f'Welcome to the List Manager! You can write "help" to get help. Version = {V} \n')
        print("Fun Fact:", fun_fact(), "\n")
    elif mode == 1:
        print(f'Welcome to the List Manager Debug Mode! You can write "help" to get help. Version = {V} \n')
    
    while True:
        start_gui()

# RUNNING PROGRAM

if __name__ == "__main__":
    main()

print(f"""
List Manager Version {V} Unofficial GUI Edition(May have some deleted features)
COPYRIGHT 2025 © Xiara Cclaere
""")
