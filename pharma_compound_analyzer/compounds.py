from file_manager import load_compounds, save_compounds
from models import Compound

def show_compounds():
    compounds = load_compounds()
    if not compounds:
        print("No compounds available.")
        return
    print("\n========== All Compounds ==========")
    for c in compounds:
        comp = Compound(c["name"], c["molecular_weight"], c["logP"], c["solubility"])
        print(comp)

def search_compound(name):
    compounds = load_compounds()
    for c in compounds:
        if c["name"].lower() == name.lower():
            comp = Compound(c["name"], c["molecular_weight"], c["logP"], c["solubility"])
            print("\nCompound found:")
            print(comp)
            return
    print("Compound not found.")

def add_compound():
    name = input("Enter compound name: ")
    try:
        mw = float(input("Enter molecular weight: "))
        logP = float(input("Enter LogP: "))
    except ValueError:
        print("Error: Molecular weight and LogP must be numbers.")
        return
    sol = input("Enter solubility: ")

    new_comp = Compound(name, mw, logP, sol)
    compounds = load_compounds()
    compounds.append(new_comp.to_dict())
    save_compounds(compounds)
    print("Compound added successfully!")


def delete_compound(name):
    compounds = load_compounds()
    updated = [c for c in compounds if c["name"].lower() != name.lower()]
    if len(updated) == len(compounds):
        print("Compound not found.")
    else:
        save_compounds(updated)
        print(f"{name} deleted successfully.")
