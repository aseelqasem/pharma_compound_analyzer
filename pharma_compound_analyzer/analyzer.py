from file_manager import load_compounds
from models import Compound

def analyze_compound(name):
    compounds = load_compounds()
    for c in compounds:
        if c["name"].lower() == name.lower():
            comp = Compound(c["name"], c["molecular_weight"], c["logP"], c["solubility"])
            print("\n========== Compound Analysis ==========")
            print(comp)

            if comp.logP > 3:
                print("LogP: High")
            elif comp.logP > 1:
                print("LogP: Moderate")
            else:
                print("LogP: Low")

            if comp.molecular_weight > 400:
                print("Molecular Weight: High")
            elif comp.molecular_weight > 200:
                print("Molecular Weight: Moderate")
            else:
                print("Molecular Weight: Low")

            print(f"Solubility: {comp.solubility}")
            return
    print("Compound not found.")

def show_statistics():
    compounds = load_compounds()
    if not compounds:
        print("No compounds available.")
        return

    total = len(compounds)
    avg_mw = sum(c["molecular_weight"] for c in compounds) / total
    avg_logP = sum(c["logP"] for c in compounds) / total

    print("\n========== Statistics ==========")
    print(f"Total compounds: {total}")
    print(f"Average Molecular Weight: {avg_mw:.2f}")
    print(f"Average LogP: {avg_logP:.2f}")

def compare_compounds(name1, name2):
    compounds = load_compounds()
    c1 = next((Compound(c["name"], c["molecular_weight"], c["logP"], c["solubility"]) for c in compounds if c["name"].lower() == name1.lower()), None)
    c2 = next((Compound(c["name"], c["molecular_weight"], c["logP"], c["solubility"]) for c in compounds if c["name"].lower() == name2.lower()), None)

    if not c1 or not c2:
        print("One or both compounds not found.")
        return

    print("\n========== Comparison ==========")
    print(f"{'':15}{c1.name:15}{c2.name:15}")
    print(f"{'MW':15}{c1.molecular_weight:<15}{c2.molecular_weight:<15}")
    print(f"{'LogP':15}{c1.logP:<15}{c2.logP:<15}")
    print(f"{'Solubility':15}{c1.solubility:<15}{c2.solubility:<15}")

def export_analysis(name, filename="analysis.txt"):
    compounds = load_compounds()
    for c in compounds:
        if c["name"].lower() == name.lower():
            comp = Compound(c["name"], c["molecular_weight"], c["logP"], c["solubility"])
            with open(filename, "w") as f:
                f.write("Compound Analysis\n")
                f.write(str(comp) + "\n")
                f.write(f"LogP: {comp.logP}\n")
                f.write(f"Molecular Weight: {comp.molecular_weight}\n")
                f.write(f"Solubility: {comp.solubility}\n")
            print(f"Analysis exported to {filename}")
            return
    print("Compound not found.")
