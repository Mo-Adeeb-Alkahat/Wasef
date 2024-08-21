import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from caption_generator import generate_caption_ar

# Function to upload and display image
def upload_image():
    global image_label, uploaded_image
    filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")]) # Display to select image
    if filename:
        image = Image.open(filename)
        # Resize image for display
        resized_image = image.resize((500, 300), Image.BICUBIC)
        photo = ImageTk.PhotoImage(resized_image)
        image_label.config(image=photo) # Display image
        image_label.image = photo  # Keep a reference for garbage collection
        uploaded_image = filename  # Store filename for caption generation

# Function to generate caption
def generate_caption():
    global uploaded_image
    if uploaded_image:
        caption_text.configure(bg="#f0f0f0") # Change label color 
        caption = generate_caption_ar(uploaded_image) # Load caption from Ai model
        caption_text.config(text=f"{caption}") # Display the caption

# Custom title bar functions
def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

def close_window():
    root.destroy()

# Initialize the main window
root = tk.Tk()
root.title("Image Caption Generator")
root.geometry("600x600")
root.overrideredirect(True)  # Remove the native title bar
root.configure(bg="#5195D3")

# Custom title bar
title_bar = tk.Frame(root, bg="#D3B751", relief="raised", bd=2)
title_bar.pack(fill=tk.X)

title_label = tk.Label(title_bar, text="Image Caption Generator", bg="#D3B751", fg="white", font=("Helvetica", 12, "bold"))
title_label.pack(side=tk.LEFT, padx=10)

close_button = tk.Button(title_bar, text="X", command=close_window, bg="#e74c3c", fg="white", bd=0, font=("Helvetica", 12, "bold"))
close_button.pack(side=tk.RIGHT, padx=10)

title_bar.bind("<B1-Motion>", move_window)

# Styles
button_style = {
    "font": ("Helvetica", 12, "bold"),
    "bg": "#D3B751",
    "fg": "#ffffff",
    "activebackground": "#45a049",
    "activeforeground": "#ffffff",
    "relief": "raised",
    "bd": 3,
    "padx": 10,
    "pady": 10
}

label_style = {
    "font": ("Helvetica", 16),
    "bg": "#f0f0f0",
    "fg": "#333333",
    "padx": 10,
    "pady": 10
}

# Upload image button
upload_button = tk.Button(root, text="Upload Image", command=upload_image, **button_style)
upload_button.pack(pady=10)

# Image label
image_label = tk.Label(root, **label_style)
image_label.pack(padx=10)
image_label.configure(bg="#5195D3")


# Caption text label
caption_text = tk.Label(root, text="", **label_style)
caption_text.pack(pady=10)
caption_text.configure(bg="#5195D3")


# Generate caption button
generate_button = tk.Button(root, text="Generate Caption", command=generate_caption, **button_style)
generate_button.pack(pady=10)

# Run the main event loop
root.mainloop()


