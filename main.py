import customtkinter
import webbrowser
import requests
import json

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.resizable(width=False, height=False)
app.geometry("400x420")
app.title("Live Currency Conversion")

def openLink():
    webbrowser.open("https://github.com/RubricLake")
def convertCurrency():
    print("Button Pressed!")
    
    # Get your own API key at https://www.exchangerate-api.com 
    link = "https://v6.exchangerate-api.com/v6/[YOUR-API-KEY-HERE]/latest/"
    origin = originEntry.get().upper()
    amount = amountEntry.get()
    destination = destinationEntry.get().upper()
    
    f = open('currencies.json','r', -1, 'utf-8')
    checkList = json.load(f)
    
    if origin not in checkList or destination not in checkList:
        resultLabel.configure(text="Invalid Currencies")
        return
    elif not amount.isnumeric():
        resultLabel.configure(text="Invalid Amount")
        return
        
    amount = float(amount)
    link = link + origin
    url = requests.get(link)
    exchange = json.loads(url.text)
    print("Requesting date from: " + link)
    print("Status Code: " + str(url.status_code))
    
    # originRate = exchange['conersion_rates'][origin] (Not Necessary)
    destinationRate = exchange['conversion_rates'][destination]
    finalAmount = round(amount * destinationRate, 2)
    amountText = str(amount), origin, "=", str(finalAmount), destination 
    resultLabel.configure(text=amountText)    
    
    
    
titleFont = customtkinter.CTkFont(family="", size=36,)
titleBox = customtkinter.CTkTextbox(app)
titleBox = customtkinter.CTkTextbox(app, fg_color="transparent", width=400, height=50, corner_radius=0, activate_scrollbars=False, font=titleFont, padx="40", pady="25")
titleBox.insert("0.0", "Currency Converter")
titleBox.configure(state="disabled")
titleBox.pack()

entryFont = customtkinter.CTkFont(family="",size=19)
originEntry = customtkinter.CTkEntry(app, placeholder_text="Origin Currency (e.g. USD)", height=45, width=300, font=entryFont)
originEntry.place(relx=0.5, rely=0.20, anchor=customtkinter.N)

amountEntry = customtkinter.CTkEntry(app, placeholder_text="Origin Amount", font=entryFont, height=45, width=300)
amountEntry.place(relx=0.5, rely=0.40, anchor=customtkinter.CENTER)

destinationEntry = customtkinter.CTkEntry(app, placeholder_text="Destination Currency (e.g. CAD)", font=entryFont, height=45, width=300, )
destinationEntry.place(relx=.5, rely=.60, anchor = customtkinter.S)


button = customtkinter.CTkButton(master=app, text="Convert", command=convertCurrency, width=290, height=40)
button.place(relx=0.5, rely=0.75, anchor=customtkinter.S)

#resultEntry = customtkinter.CTkEntry(app, justify=customtkinter.CENTER, font=entryFont, height=35, width=300, state="normal", bg_color='transparent')
#resultEntry.place(relx=.5, rely=.83, anchor = customtkinter.CENTER)
#resultEntry.insert(0, "Results")

resultLabel = customtkinter.CTkLabel(app, height=35, width=300, bg_color='transparent', justify='center', font=customtkinter.CTkFont('Consolas', 25), text="")
resultLabel.place(relx=.5, rely=.83, anchor=customtkinter.CENTER)

link = customtkinter.CTkLabel(app, text="Made by Ethan Kigotho", cursor="hand2", text_color="grey", fg_color='transparent', bg_color='transparent', justify='center', font=('Consolas', 15, "underline"))
link.place(relx=.30, rely=.9)
link.bind("<Button-1>", lambda e: openLink())

app.mainloop()