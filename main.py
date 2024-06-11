import os
import shutil
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk


class ImageSorter:
  def __init__(self, master):
    self.master = master
    self.max_width = 1200
    self.max_height = 800
    self.min_width = 800
    self.min_height = 600
    master.title("Image Sorter")
    
    self.label = Label(master, text="Review the image and choose Yes or No")
    self.label.pack()
    
    self.image_label = Label(master)
    self.image_label.pack()
    
    self.yes_button = Button(master, text="Yes", command=self.move_image)
    self.yes_button.pack(side="left")
    self.master.bind("<y>", self.move_image)
    
    self.no_button = Button(master, text="No", command=self.next_image)
    self.no_button.pack(side="right")
    self.master.bind("<n>", self.next_image)
    
    self.source_dir = filedialog.askdirectory(title="Select Source Directory")
    self.dest_dir = filedialog.askdirectory(title="Select Destination Directory")

    if not self.source_dir or not self.dest_dir:
      self.label.config(text="Please select source and destination directories.")
      return self.master.destroy()
    
    self.image_files = [f for f in os.listdir(self.source_dir) if f.endswith(('jpg', 'png', 'jpeg'))]
    self.current_image = None
    self.load_next_image()

  def load_next_image(self):
    if self.image_files:
      self.current_image = self.image_files.pop(0)
      image_path = os.path.join(self.source_dir, self.current_image)
      image = Image.open(image_path)
      image.thumbnail((self.max_width, self.max_height), Image.Resampling.LANCZOS)
      photo = ImageTk.PhotoImage(image)
      self.image_label.config(image=photo)
      self.image_label.image = photo
    else:
      self.label.config(text="No more images to review.")
  
  def move_image(self, event=None):
    if self.current_image:
      shutil.move(os.path.join(self.source_dir, self.current_image), os.path.join(self.dest_dir, self.current_image))
    self.load_next_image()
  
  def next_image(self, event=None):
    self.load_next_image()


root = Tk()
image_sorter = ImageSorter(root)
root.mainloop()
