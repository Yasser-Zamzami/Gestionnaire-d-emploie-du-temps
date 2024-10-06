from tkinter import Tk, Canvas, Button, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_file_1():
    window.destroy()
    import ajouter_formateur

def open_file_2():
    window.destroy()
    import ajouter_groupe

def open_file_3():
    window.destroy()
    import ajouter_salle

def open_file_4():
    window.destroy()
    import create_emploi



window = Tk()

window.geometry("850x600")
window.configure(bg="#69F0F8")
window.title("configuration")
window.iconbitmap("calendar.ico")

canvas = Canvas(
    window,
    bg="#69F0F8",
    height=600,
    width=950,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    359.0,
    285.0,
    image=image_image_1
)

canvas.create_rectangle(
    316.0,
    0.0,
    950.0,
    600.0,
    fill="#D9D9D9",
    outline=""
)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_file_4,
    relief="flat"
)
button_1.place(
    x=342.0,
    y=305.0,
    width=368.0,
    height=37.0
)



button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=open_file_3,
    relief="flat"
)
button_3.place(
    x=342.0,
    y=219.0,
    width=368.0,
    height=37.0
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=open_file_2,
    relief="flat"
)
button_4.place(
    x=342.0,
    y=125.0,
    width=368.0,
    height=37.0
)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=open_file_1,
    relief="flat"
)
button_5.place(
    x=342.0,
    y=39.0,
    width=368.0,
    height=37.0
)

window.resizable(False, False)
window.mainloop()
