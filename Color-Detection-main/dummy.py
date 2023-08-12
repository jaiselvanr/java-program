from tkinter import *
from tkinter import filedialog

# Create a popup window for user input
root = Tk()
root.title("Image and Cluster Count Input")

# Function to get image file path using filedialog
def get_image():
    image_path = filedialog.askopenfilename(initialdir="/", title="Select Image File", filetypes=(("JPEG Files", "*.jpg"), ("PNG Files", "*.png"), ("All Files", "*.*")))
    return image_path

# Function to get cluster count input
def get_cluster_count():
    cluster_count = int(cluster_count_entry.get())
    root.destroy()  # Close the popup window
    return cluster_count

# Label for cluster count input
cluster_count_label = Label(root, text="Cluster Count:")
cluster_count_label.pack()

# Entry for cluster count input
cluster_count_entry = Entry(root)
cluster_count_entry.pack()

# Button to get image file path
image_button = Button(root, text="Select Image", command=get_image)
image_button.pack()

# Button to submit input and close the popup window
submit_button = Button(root, text="Submit", command=get_cluster_count)
submit_button.pack()

root.mainloop()  # Run the popup window
