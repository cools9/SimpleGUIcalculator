import customtkinter as ctk
import pywinstyles

window=ctk.CTk()
pywinstyles.apply_style(window, "acrylic")


window.geometry("500x500")
window.title("GUI CALCULATOR")
window.mainloop()
