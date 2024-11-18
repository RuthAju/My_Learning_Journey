import qrcode
from tkinter import Tk, colorchooser

class Color_picker:

    # Hides the main tkinter window
    Tk().withdraw()
    def __init__(self):
        # Prompt user for data and file information
        self.data = input("Enter the data to encode: ")
        self.path = input("Enter the destination path: ")
        self.file_name = input("Enter the name to save the image: ")

        # Color selection for background and fill
        self.b_color = colorchooser.askcolor(title= "Select background color")[1]  # Ask the user to choose a color and get the hex code
        print(f"Selected background color hexcode: {self.b_color}")

        self.f_color = colorchooser.askcolor(title="Select a fill color")[1]
        print(f"Selected fill color hexcode: {self.f_color}")

        # Check if background and fill colors are the same
        if self.b_color == self.f_color:
            print("Error: Background color is the same as fill color.")
            exit()
        else:
            self.generate_qr_code()


    def generate_qr_code(self):

        # Set up the QR code with error correction and sizing
        qr = qrcode.QRCode(
            version= 1,
            box_size=10,
            border= 4
        )

        # Replace backslashes in the path for python compatibility
        self.path = self.path.replace("\\","/")
        self.path = self.path + "/" + self.file_name + ".png"

        qr.add_data(self.data)
        qr.make(fit=True)

        # Generate the image with selected colors
        img = qr.make_image(fill_color= self.f_color, back_color= self.b_color)
        img.save(self.path)
        print("Qr code generated successfully!")
        
qr_code = Color_picker()



