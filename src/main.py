# src/main.py

import os
import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.ttk as ttk
from color_parser import parse_colors
from atlas_generator import ColorAtlasGenerator

class ColorAtlasApp:
    def __init__(self, master):
        self.master = master
        master.title("Color Atlas Generator")

        # File selection UI
        self.file_label = tk.Label(master, text="No file selected", width=50, anchor="w")
        self.file_label.pack(pady=5)
        self.select_file_button = tk.Button(master, text="Select Colors File", command=self.select_file)
        self.select_file_button.pack(pady=5)

        # Canvas dimensions entry UI
        dimensions_frame = tk.Frame(master)
        dimensions_frame.pack(pady=5)

        self.width_label = tk.Label(dimensions_frame, text="Canvas Width:")
        self.width_label.pack(side=tk.LEFT, padx=(0, 5))
        self.width_entry = tk.Entry(dimensions_frame, width=8)
        self.width_entry.insert(0, "128")  # Default width set to 128
        self.width_entry.pack(side=tk.LEFT, padx=(0, 15))

        self.height_label = tk.Label(dimensions_frame, text="Canvas Height:")
        self.height_label.pack(side=tk.LEFT, padx=(0, 5))
        self.height_entry = tk.Entry(dimensions_frame, width=8)
        self.height_entry.insert(0, "128")  # Default height set to 128
        self.height_entry.pack(side=tk.LEFT)

        # Generate button UI
        self.generate_button = tk.Button(master, text="Generate PNG", command=self.generate_png)
        self.generate_button.pack(pady=10)

        # Open PNG button UI
        self.open_png_button = tk.Button(master, text="Open PNG", command=self.open_png)
        self.open_png_button.pack(pady=5)

        # Credit label at the bottom left
        self.credit_label = tk.Label(master, text="Made by: @NAWIDX", anchor="w")
        self.credit_label.pack(side=tk.BOTTOM, anchor="w", padx=5, pady=5)

        # Internal variables
        self.colors_file_path = None
        self.output_file = "color_atlas.png"

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Colors HEX File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.colors_file_path = file_path
            self.file_label.config(text=file_path)

    def generate_png(self):
        if not self.colors_file_path:
            messagebox.showerror("Error", "Please select a colors file first.")
            return

        try:
            canvas_width = int(self.width_entry.get())
            canvas_height = int(self.height_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for canvas dimensions.")
            return

        colors = parse_colors(self.colors_file_path)
        if not colors:
            messagebox.showerror("Error", "No colors found in the selected file.")
            return

        atlas_generator = ColorAtlasGenerator(colors)
        atlas_generator.create_png(canvas_width, canvas_height, self.output_file)
        messagebox.showinfo("Success", "Color atlas generated successfully!")

    def open_png(self):
        if os.path.exists(self.output_file):
            os.startfile(self.output_file)
        else:
            messagebox.showerror("Error", f"{self.output_file} does not exist. Please generate it first.")

def main():
    root = tk.Tk()
    app = ColorAtlasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()