import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("animal_classification_model.h5")

class_names = [
    "Bear", "Bird", "Cat", "Cow", "Deer",
    "Dog", "Dolphin", "Elephant", "Giraffe", "Horse",
    "Kangaroo", "Lion", "Panda", "Tiger", "Zebra"
]

CONFIDENCE_THRESHOLD = 0.50

def preprocess_image(image_path):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

def predict_animal(image_path):
    img_array = preprocess_image(image_path)
    predictions = model.predict(img_array)
    confidence = np.max(predictions)
    predicted_class = np.argmax(predictions, axis=1)[0]

    if confidence >= CONFIDENCE_THRESHOLD:
        return class_names[predicted_class], confidence * 100
    else:
        return "Unable to detect", confidence * 100

def on_file_drop(event):
    file_path = event.data.strip("{}")
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

        animal, confidence = predict_animal(file_path)
        if animal == "Unable to detect":
            result_label.config(text="I am unable to detect that.")
        else:
            result_label.config(text=f"Prediction: {animal} ({confidence:.2f}% confidence)")
    else:
        result_label.config(text="Invalid file type. Please drop an image file.")

def clear_interface():
    image_label.config(image=None)
    image_label.image = None
    result_label.config(text="")
    instruction_label.config(text="Drag and drop an image here")

root = TkinterDnD.Tk()
root.title("Animal Detection")
root.geometry("400x450")

instruction_label = tk.Label(root, text="Drag and drop an image here", font=("Arial", 14))
instruction_label.pack(pady=20)

image_label = tk.Label(root)
image_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

clear_button = tk.Button(root, text="Clear", font=("Arial", 12), command=clear_interface)
clear_button.pack(pady=10)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_file_drop)

root.mainloop()
