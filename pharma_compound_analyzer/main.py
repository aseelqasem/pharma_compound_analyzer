from utils import show_menu
from compounds import show_compounds, search_compound, add_compound, delete_compound
from analyzer import analyze_compound, show_statistics, compare_compounds, export_analysis

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            show_compounds()
        elif choice == "2":
            name = input("Enter compound name: ")
            search_compound(name)
        elif choice == "3":
            add_compound()
        elif choice == "4":
            name = input("Enter compound name to delete: ")
            delete_compound(name)
        elif choice == "5":
            name = input("Enter compound name to analyze: ")
            analyze_compound(name)
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            name1 = input("Enter first compound name: ")
            name2 = input("Enter second compound name: ")
            compare_compounds(name1, name2)
        elif choice == "8":
            name = input("Enter compound name to export analysis: ")
            export_analysis(name)
        elif choice == "9":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
