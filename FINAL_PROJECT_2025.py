# Unit Converter

import tkinter as tk
from tkinter import ttk, messagebox

# Ovo ovdje su sve funkcije za pretvaranje

# Funkcija za pretvaranje temperature
def pretvaranje_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Funkcija za pretvaranje dužine
def pretvaranje_duzine(value, from_unit, to_unit):
    jedinice_duzine = {
        'Kilometres': 0.001, 'Metres': 1, 'Centimetres': 100,
        'Millimetres': 1000, 'Miles': 0.000621, 'Yards': 1.094,
        'Feet': 3.28084, 'Inches': 39.37, 'Nautical miles': 0.00054
    }
    return value * jedinice_duzine[to_unit] / jedinice_duzine[from_unit]

# Funkcija za pretvaranje mase
def pretvaranje_mase(value, from_unit, to_unit):
    jedinice_mase = {
        'Kilograms': 1, 'Grams': 1000, 'Milligrams': 1000000,
        'Pounds': 0.453592, 'Ounces': 0.0283495, 'Carats': 5000,
        'Tons (metric)': 0.001
    }
    return value * jedinice_mase[to_unit] / jedinice_mase[from_unit]

# Funkcija za pretvaranje zapremine
def pretvaranje_zapremine(value, from_unit, to_unit):
    jedinice_zapremine = {
        'Cubic meters': 1, 'Cubic centimeters': 1000000,
        'Liters': 1000, 'Milliliters': 1000000,
        'Gallons (US)': 264.1721, 'Quarts (US)': 1056.688,
        'Pints (US)': 2113.376, 'Fluid ounces (US)': 33814.02,
        'Cubic inches': 61023.74
    }
    return value * jedinice_zapremine[to_unit] / jedinice_zapremine[from_unit]

# Funkcija za pretvaranje energije
def pretvaranje_energije(value, from_unit, to_unit):
    jedinice_energije = {
        'Joules': 1, 'Kilojoules': 0.001, 'Calories': 0.000239,
        'Kilocalories': 0.239, 'Watt-hours': 0.000279,
        'Kilowatt-hours': 0.0000003, 'BTU': 0.001
    }
    return value * jedinice_energije[to_unit] / jedinice_energije[from_unit]

# Funkcija za pretvaranje brzine
def pretvaranje_brzine(value, from_unit, to_unit):
    jedinice_brzine = {
        'Meters per second': 1, 'Kilometers per hour': 3.6,
        'Miles per hour': 2.23694, 'Feet per second': 3.28084,
        'Knots': 1.94384
    }
    return value * jedinice_brzine[to_unit] / jedinice_brzine[from_unit]

# Funkcija za pretvaranje vremena
def pretvaranje_vremena(value, from_unit, to_unit):
    jedinice_vremena = {
        'Seconds': 1, 'Minutes': 0.0167, 'Hours': 0.000277778,
        'Days': 0.0000115741, 'Weeks': 0.00000165344,
        'Months': 0.00000038052, 'Years': 3.17098e-8,
        'Milliseconds': 1000, 'Microseconds': 1000000,
        'Nanoseconds': 1e9, 'Picoseconds': 1e12, 'Femtoseconds': 1e15,
    }
    return value * jedinice_vremena[to_unit] / jedinice_vremena[from_unit]

# Funkcija za pretvaranje površine
def pretvaranje_povrsine(value, from_unit, to_unit):
    jedinice_povrsine = {
        'Square meters': 1, 'Square kilometers': 0.000001,
        'Hectares': 0.0001, 'Acres': 0.000247105,
        'Square feet': 10.7639, 'Square yards': 1.19599,
        'Square miles': 3.861e-7, 'Square centimeters': 10000,
        'Square millimeters': 1000000, 'Square inches': 1550.0031
    }
    return value * jedinice_povrsine[to_unit] / jedinice_povrsine[from_unit]

# Funkcija za pretvaranje snage
def pretvaranje_snage(value, from_unit, to_unit):
    jedinice_snage = {
        'Watts': 1, 'Kilowatts': 0.001, 'Horsepower': 0.00134102,
        'BTU per hour': 0.000293071, 'Calories per second': 0.239006
    }
    return value * jedinice_snage[to_unit] / jedinice_snage[from_unit]

# Funkcija za pretvaranje pritiska
def pretvaranje_pritiska(value, from_unit, to_unit):
    jedinice_pritiska = {
        'Pascals': 1, 'Kilopascals': 1000, 'Bar': 100000,
        'Atmospheres': 101.325, 'Torr': 133.322, 'Psi': 6894.76
    }
    return value * jedinice_pritiska[to_unit] / jedinice_pritiska[from_unit]

# Funkcija za pretvaranje kuta
def pretvaranje_kuta(value, from_unit, to_unit):
    jedinice_kuta = {
        'Degrees': 1, 'Radians': 57.2958, 'Gradians': 0.9
    }
    return value * jedinice_kuta[to_unit] / jedinice_kuta[from_unit]

# Funkcija za pretvaranje podataka
def pretvaranje_podataka(value, from_unit, to_unit):
    jedinice_podataka = {
        'Bits': 1, 'Bytes': 0.8, 'Kilobits': 0.001, 'Kilobytes': 0.008,
        'Megabits': 0.000001, 'Megabytes': 0.000008,
        'Gigabits': 0.000000001, 'Gigabytes': 0.000000008,
        'Terabits': 0.000000000001, 'Terabytes': 0.000000000008,
        'Petabytes': 0.000000000000008
    }
    return value * jedinice_podataka[to_unit] / jedinice_podataka[from_unit]

# A ovo je funkcija za pretvaranje jedinica

def pretvori():
    try:
        value = float(ulazna_vrijednost.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        
        if combo_kategorija.get() == 'Temperature':
            result = pretvaranje_temperature(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Length':
            result = pretvaranje_duzine(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Mass':
            result = pretvaranje_mase(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Volume':
            result = pretvaranje_zapremine(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Energy':
            result = pretvaranje_energije(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Speed':
            result = pretvaranje_brzine(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Time':
            result = pretvaranje_vremena(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Area':
            result = pretvaranje_povrsine(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Power':
            result = pretvaranje_snage(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Pressure':
            result = pretvaranje_pritiska(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Angle':
            result = pretvaranje_kuta(value, from_unit, to_unit)
        elif combo_kategorija.get() == 'Data':
            result = pretvaranje_podataka(value, from_unit, to_unit)
        
        label_result.config(text=f"Result: {result:.4f} {to_unit}")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid value.")
        
# Ovo je funkcija da se promjene jedinice ako korisnik promjeni kategoriju

def update_jedinice(_):
    kategorija = combo_kategorija.get()
    jedinice = {
        'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin'],
        'Length': ['Kilometres', 'Metres', 'Centimetres', 'Millimetres', 'Miles', 'Yards', 'Feet', 'Inches', 'Nautical miles'],
        'Mass': ['Kilograms', 'Grams', 'Milligrams', 'Pounds', 'Ounces', 'Carats', 'Tons (metric)'],
        'Volume': ['Cubic meters', 'Cubic centimeters', 'Liters', 'Milliliters', 'Gallons (US)', 'Quarts (US)', 'Pints (US)', 'Fluid ounces (US)', 'Cubic inches'],
        'Energy': ['Joules', 'Kilojoules', 'Calories', 'Kilocalories', 'Watt-hours', 'Kilowatt-hours', 'BTU'],
        'Speed': ['Meters per second', 'Kilometers per hour', 'Miles per hour', 'Feet per second', 'Knots'],
        'Time': ['Seconds', 'Minutes', 'Hours', 'Days', 'Weeks', 'Months', 'Years', 'Milliseconds', 'Microseconds', 'Nanoseconds', 'Picoseconds', 'Femtoseconds'],
        'Area': ['Square meters', 'Square kilometers', 'Hectares', 'Acres', 'Square feet', 'Square yards', 'Square miles', 'Square centimeters', 'Square millimeters', 'Square inches'],
        'Power': ['Watts', 'Kilowatts', 'Horsepower', 'BTU per hour', 'Calories per second'],
        'Pressure': ['Pascals', 'Kilopascals', 'Bar', 'Atmospheres', 'Torr', 'Psi'],
        'Angle': ['Degrees', 'Radians', 'Gradians'],
        'Data': ['Bits', 'Bytes', 'Kilobits', 'Kilobytes', 'Megabits', 'Megabytes', 'Gigabits', 'Gigabytes', 'Terabits', 'Terabytes', 'Petabytes']
    }
    combo_from['values'] = jedinice.get(kategorija, [])
    combo_to['values'] = jedinice.get(kategorija, [])
    combo_from.set(jedinice[kategorija][0])
    combo_to.set(jedinice[kategorija][1])
    
# Ovdje pravimo glavni prozor

root = tk.Tk()
root.title("Unit Converter")
root.config(bg='#222222')

# Ovo su ulazne vrijednosti

frame_top = tk.Frame(root, bg='#222222', padx=10, pady=10)
frame_top.pack(fill='x')

tk.Label(frame_top, text='Enter value: ', bg='#222222', fg='white').pack(side='left', padx=5, pady=5)
ulazna_vrijednost = tk.Entry(frame_top, width=10, bg='#333333', fg='white')
ulazna_vrijednost.pack(side='left', padx=5, pady=5)

# Ovdje pravimo meni za kategorije

frame_kategorija = tk.Frame(root, bg='#222222', padx=10, pady=10)
frame_kategorija.pack(fill='x')

tk.Label(frame_kategorija, text='Select category: ', bg='#222222', fg='white').pack(side='left', padx=5, pady=5)
combo_kategorija = ttk.Combobox(frame_kategorija, values=[
    'Temperature', 'Length', 'Mass', 'Volume',
    'Energy', 'Speed', 'Time', 'Area',
    'Power', 'Pressure', 'Angle', 'Data'
], state='readonly')
combo_kategorija.set('Temperature')
combo_kategorija.pack(side='left', padx=5, pady=5)
combo_kategorija.bind("<<ComboboxSelected>>", update_jedinice)

# Ovdje pravimo meni za jedinice

frame_jedinice = tk.Frame(root, bg='#222222', padx=10, pady=10)
frame_jedinice.pack(fill='x')

tk.Label(frame_jedinice, text='From: ', bg='#222222', fg='white').pack(side='left', padx=5, pady=5)
combo_from = ttk.Combobox(frame_jedinice, state='readonly')
combo_from.pack(side='left', padx=5, pady=5)

tk.Label(frame_jedinice, text='To: ', bg='#222222', fg='white').pack(side='left', padx=5, pady=5)
combo_to = ttk.Combobox(frame_jedinice, state='readonly')
combo_to.pack(side='left', padx=5, pady=5)

# Ovo je button za pretvaranje

frame_pretvori = tk.Frame(root, bg='#222222', padx=10, pady=10)
frame_pretvori.pack(fill='x')

btn_pretvori = tk.Button(frame_pretvori, text='Convert', command=pretvori, bg='#444444', fg='white')
btn_pretvori.pack(side='left', padx=5, pady=5)

# Ovdje se prikaže rezultat

frame_rezultat = tk.Frame(root, bg='#222222', padx=10, pady=10)
frame_rezultat.pack(fill='x')

label_result = tk.Label(frame_rezultat, text='Converted value: ', bg='#222222', fg='white')
label_result.pack(side='left', padx=5, pady=5)

update_jedinice(None)

# I na kraju ovom funkcijom pokrećemo aplikaciju

root.mainloop()
