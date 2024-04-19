import tkinter as tk
from tkinter import ttk
import csv

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Window")

        self.left_frame = tk.Frame(root, bg='white', width=300, height=300)
        self.right_frame = tk.Frame(root, bg='lightgrey', width=100, height=300)

        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        self.display_image()

        self.create_right_frame_widgets()

    def display_image(self):
        image_path = "screen.png"  # Provide the path to your image
        self.image = tk.PhotoImage(file=image_path)
        self.image_label = tk.Label(self.left_frame, image=self.image)
        self.image_label.pack()

    def create_right_frame_widgets(self):
        options = ["Respiratory Rate", "VTe", "FiO2", "PINSP", "PEEP", "PIP", "SP02"]
        self.option_var = tk.StringVar()
        self.option_menu = ttk.OptionMenu(self.right_frame, self.option_var, *options)
        self.option_menu.grid(row=0, column=0, padx=10, pady=10)

        self.entry_label = tk.Label(self.right_frame, text="Enter Data:")
        self.entry_label.grid(row=1, column=0, padx=10, pady=10)

        self.entry_var = tk.StringVar()
        self.entry_field = tk.Entry(self.right_frame, textvariable=self.entry_var)
        self.entry_field.grid(row=2, column=0, padx=10, pady=10)

        self.submit_button = tk.Button(self.right_frame, text="Submit", command=self.export_to_csv)
        self.submit_button.grid(row=3, column=0, padx=10, pady=10)

    def export_to_csv(self):
        data = {
            "Option": self.option_var.get(),
            "Entry": self.entry_var.get()
        }
        with open("data.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Option", "Entry"])
            writer.writerow(data)
        print("Data exported to CSV!")

if __name__ == "__main__":
    root = tk.Tk()
    window = MainWindow(root)
    root.mainloop()
