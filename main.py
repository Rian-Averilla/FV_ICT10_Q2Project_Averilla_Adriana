from pyscript import document,display

grade_8 = {"ayrton co", "duchess baetiong", "jaeden elequin", "zoe zabala", "sophia georgina celi", "reese ancheta"}
grade_9 = {"krishna kiyomi pascua", "anthony cases", "cloud toribio", "corral lara georgina", "curbi charlene faith", "ethan feudo", "ethan james de leon", "hannah galapon", "juan carlos paguio espiritu", "lacaya frances venice", "nicole repolona", "noelle acuna", "sean obcemea"}
grade_10 = {"adriana averilla", "ciara r de guzman", "dustin cunanan", "ian salangsang", "rafael iñigo roncal", "zyrene nieto"}
grade_11 = {"gianna entrada", "liam lopez", "riso salapunen", "sofia guevarra"}
grade_12 = {"enrique gerard jocson"}

members = grade_8 | grade_9 | grade_10 | grade_11 | grade_12

def add_member():
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    if not first_name or not last_name:
        display("Please enter both names.", target="result")
        return

    full_name = f"{first_name} {last_name}".lower()

    if full_name in members:
        display("Member already exists.", target="result")
    else:
        members.add(full_name)
        display(f"Member added: {full_name.title()}", target="result")

def check_member():
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    if not first_name or not last_name:
        display("Please enter both names.", target="result")
        return

    full_name = f"{first_name} {last_name}".lower()

    if full_name in members:
        display("This person is a club member.", target="result")
    else:
        display("This person is not in the club.", target="result")



def checkdeets():
    Element1 = document.getElementById("Elemsymbol")
    symbol = Element1.value.strip().capitalize()
    element_display = Nonmetals.get(symbol, ("Element not found", "-", "-"))
    display(element_display, target="output1")

    #All Nonmetals Variable
Nonmetals = {
        "H": ("Hydrogen", 1, 1.0078),
        "He": ("Helium", 2, 4.0026),
        "C": ("Carbon", 6, 12.011),
        "N": ("Nitrogen", 7, 14.007),
        "O": ("Oxygen", 8, 15.999),
        "F": ("Fluorine", 9, 18.998),
        "Ne": ("Neon", 10, 20.180),
        "P": ("Phosphorus", 15, 30.974),
        "S": ("Sulfur", 16, 32.065),
        "Cl": ("Chlorine", 17, 35.453),
        "Ar": ("Argon", 18, 39.948),
        "As": ("Arsenic", 33, 74.922),
        "Se": ("Selenium", 34, 78.971),
        "Br": ("Bromine", 35, 79.904),
        "Kr": ("Krypton", 36, 83.798),
        "I": ("Iodine", 53, 126.90),
        "Xe": ("Xenon", 54, 131.290),
        "Rn": ("Radon", 86, 222.000),
        "Og": ("Oganesson", 118, 294.000)
        }

#DISPLAY FORMAT
document.getElementById("result").innerHTML = f"""
<b> Symbol: <b> {symbol} <br>
<b> Element: <b> {element_display[0]} <br>
<b> Atomic Number: <b> {element_display[1]} <br>
<b> Atomic Mass: <b> {element_display[2]} <br>
"""