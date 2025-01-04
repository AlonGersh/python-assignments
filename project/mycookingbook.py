import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import json
import requests
from io import BytesIO

# Directory to store recipes
if not os.path.exists("data"):
    os.makedirs("data")

RECIPE_FILE = "data/recipes.json"

# Load recipes from file
if os.path.exists(RECIPE_FILE):
    with open(RECIPE_FILE, "r") as file:
        recipes = json.load(file)
else:
    recipes = []

# Save recipes to file
def save_recipes():
    with open(RECIPE_FILE, "w") as file:
        json.dump(recipes, file, indent=4)

# Function to add copy-paste functionality
def add_copy_paste_shortcuts(widget):
    widget.bind("<Control-c>", lambda e: widget.event_generate("<<Copy>>"))
    widget.bind("<Control-x>", lambda e: widget.event_generate("<<Cut>>"))
    widget.bind("<Control-v>", lambda e: widget.event_generate("<<Paste>>"))

# Main Application
class RecipeOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Organizer")

        # Category Buttons Frame
        self.category_frame = ttk.Frame(root)
        self.category_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        self.categories = ["Main", "Dessert", "Bread"]
        self.category_buttons = {}
        for category in self.categories:
            button = ttk.Button(self.category_frame, text=category, command=lambda c=category: self.filter_recipes(c))
            button.pack(side=tk.LEFT, padx=5)
            self.category_buttons[category] = button

        # Recipe List Frame
        self.recipe_list_frame = ttk.Frame(root)
        self.recipe_list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.recipe_listbox = tk.Listbox(self.recipe_list_frame, height=20, width=40)
        self.recipe_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.recipe_listbox.bind("<Double-1>", self.view_recipe)

        self.scrollbar = ttk.Scrollbar(self.recipe_list_frame, orient=tk.VERTICAL, command=self.recipe_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.recipe_listbox.config(yscrollcommand=self.scrollbar.set)

        # Buttons Frame
        self.buttons_frame = ttk.Frame(root)
        self.buttons_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.add_button = ttk.Button(self.buttons_frame, text="Add Recipe", command=self.add_recipe)
        self.add_button.pack(pady=10)

        self.view_button = ttk.Button(self.buttons_frame, text="View Recipe", command=self.view_recipe)
        self.view_button.pack(pady=10)

        self.delete_button = ttk.Button(self.buttons_frame, text="Delete Recipe", command=self.delete_recipe)
        self.delete_button.pack(pady=10)

        # Initialize filtered category to show all recipes
        self.filtered_category = None
        self.update_recipe_list()

    def filter_recipes(self, category):
        self.filtered_category = category
        self.update_recipe_list()

    def update_recipe_list(self):
        self.recipe_listbox.delete(0, tk.END)
        filtered_recipes = recipes if self.filtered_category is None else [r for r in recipes if r["category"] == self.filtered_category]
        for recipe in filtered_recipes:
            self.recipe_listbox.insert(tk.END, recipe["name"])

    def add_recipe(self):
        AddRecipeWindow(self)

    def view_recipe(self, event=None):
        selected_index = self.recipe_listbox.curselection()
        if selected_index:
            ViewRecipeWindow(self, selected_index[0])
        else:
            messagebox.showinfo("Info", "Please select a recipe to view.")

    def delete_recipe(self):
        selected_index = self.recipe_listbox.curselection()
        if selected_index:
            del recipes[selected_index[0]]
            save_recipes()
            self.update_recipe_list()
            messagebox.showinfo("Success", "Recipe deleted successfully.")
        else:
            messagebox.showinfo("Info", "Please select a recipe to delete.")

class AddRecipeWindow:
    def __init__(self, app):
        self.app = app
        self.window = tk.Toplevel()
        self.window.title("Add Recipe")

        ttk.Label(self.window, text="Recipe Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = ttk.Entry(self.window, width=30, justify="right")
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        add_copy_paste_shortcuts(self.name_entry)

        ttk.Label(self.window, text="Category:").grid(row=1, column=0, padx=10, pady=5)
        self.category_combobox = ttk.Combobox(self.window, values=self.app.categories, state="readonly", width=28)
        self.category_combobox.grid(row=1, column=1, padx=10, pady=5)
        self.category_combobox.set(self.app.categories[0])

        ttk.Label(self.window, text="Instructions:").grid(row=2, column=0, padx=10, pady=5)
        self.instructions_text = tk.Text(self.window, width=30, height=10, wrap=tk.WORD)
        self.instructions_text.tag_configure("right", justify="right")
        self.instructions_text.grid(row=2, column=1, padx=10, pady=5)
        add_copy_paste_shortcuts(self.instructions_text)

        ttk.Label(self.window, text="Video Link (Optional):").grid(row=3, column=0, padx=10, pady=5)
        self.video_entry = ttk.Entry(self.window, width=30, justify="right")
        self.video_entry.grid(row=3, column=1, padx=10, pady=5)
        add_copy_paste_shortcuts(self.video_entry)

        ttk.Label(self.window, text="Image (Optional):").grid(row=4, column=0, padx=10, pady=5)
        self.image_path = tk.StringVar()
        self.image_entry = ttk.Entry(self.window, textvariable=self.image_path, width=30, justify="right")
        self.image_entry.grid(row=4, column=1, padx=10, pady=5)
        add_copy_paste_shortcuts(self.image_entry)
        ttk.Label(self.window, text="(File path or URL)").grid(row=4, column=2, padx=5, pady=5)

        ttk.Button(self.window, text="Save Recipe", command=self.save_recipe).grid(row=5, column=1, pady=10)

    def save_recipe(self):
        name = self.name_entry.get()
        category = self.category_combobox.get()
        instructions = self.instructions_text.get("1.0", tk.END).strip()
        video_link = self.video_entry.get()
        image = self.image_path.get()

        if not name:
            messagebox.showerror("Error", "Recipe name is required.")
            return

        recipe = {
            "name": name,
            "category": category,
            "instructions": instructions,
            "video_link": video_link,
            "image": image,
            "comments": []
        }
        recipes.append(recipe)
        save_recipes()
        self.app.update_recipe_list()
        self.window.destroy()
        messagebox.showinfo("Success", "Recipe added successfully.")

class ViewRecipeWindow:
    def __init__(self, app, recipe_index):
        self.app = app
        self.recipe_index = recipe_index
        self.recipe = recipes[recipe_index]

        self.window = tk.Toplevel()
        self.window.title(self.recipe["name"])

        ttk.Label(self.window, text=f"Category: {self.recipe['category']}").pack(pady=5)
        ttk.Label(self.window, text="Instructions:").pack()

        instructions_text = tk.Text(self.window, wrap=tk.WORD, height=10, width=40)
        instructions_text.insert(tk.END, self.recipe["instructions"])
        instructions_text.tag_configure("right", justify="right")
        instructions_text.config(state=tk.DISABLED)
        instructions_text.pack(pady=5)

        if self.recipe.get("video_link"):
            ttk.Label(self.window, text=f"Video Link: {self.recipe['video_link']}").pack(pady=5)

        if self.recipe.get("image"):
            self.display_image(self.recipe["image"])

        ttk.Label(self.window, text="Comments:").pack()
        self.comments_listbox = tk.Listbox(self.window, height=5, width=40)
        for comment in self.recipe["comments"]:
            self.comments_listbox.insert(tk.END, comment)
        self.comments_listbox.pack(pady=5)

        self.new_comment_entry = ttk.Entry(self.window, width=40, justify="right")
        self.new_comment_entry.pack(pady=5)
        add_copy_paste_shortcuts(self.new_comment_entry)
        ttk.Button(self.window, text="Add Comment", command=self.add_comment).pack(pady=5)

    def display_image(self, image_source):
        try:
            if image_source.startswith("http"):
                response = requests.get(image_source)
                img_data = BytesIO(response.content)
                img = Image.open(img_data)
            else:
                img = Image.open(image_source)

            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            img_label = ttk.Label(self.window, image=img)
            img_label.image = img
            img_label.pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def add_comment(self):
        comment = self.new_comment_entry.get()
        if comment:
            self.recipe["comments"].append(comment)
            save_recipes()
            self.comments_listbox.insert(tk.END, comment)
            self.new_comment_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeOrganizerApp(root)
    root.mainloop()
