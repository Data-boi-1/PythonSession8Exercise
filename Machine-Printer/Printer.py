import os
from Machine import Machine
from PaperTray import PaperTray

#Printer klassen arver fra Machine klassen vha. super().__init__()
class Printer(Machine):
    def __init__(self):
        super().__init__()
        self.paper_tray = PaperTray()
        self.folder_path = "Document_folder"

        #Laver en mappe hvis den ikke allerede eksisterer
        if not os.path.exists(self.folder_path):
           os.mkdir(self.folder_path)
    #opretter et dokument i folderen "Document_folder" hvis self.paper_tray.paper_count > 0 (hvis der er papir i printeren)
    #samtidigt med at printeren er tændt: self.powered_on
    #self.paper_tray.use_paper(1) bruges til at trække et papir fra printeren, men hvis den er tom
    #så skriver den at der ikke er mere papir
    def print_document(self, document):
        if self.powered_on:
            if self.paper_tray.paper_count > 0:
                print("Printing the following document:")
                print(document)
                self.paper_tray.use_paper(1)
                self.save_document_to_file(document)
            else:
                print("Printer is empty of paper. Please load more paper to print")
        else:
            print("Printer is not powered on. Please turn it on to print")
    #Gemmer dokumentet i folderen "Document_folder" som en .txt fil
    def save_document_to_file(self, document):
        file_path = os.path.join(self.folder_path, "document.txt")
        with open(file_path, "a") as file:
            file.write(document + "\n")
            print(f"Document saved to '{file_path}'.")
    #load_paper er lavet i PaperTray.py og bliver kaldt her
    def load_paper(self, count):
        self.paper_tray.load_paper(count)

#User input
#Opgaven er lavet, men har tilføjet user input, så man selv kan tænde, slukke og fylde papir
#Derudover er der også lavet en input-choice for at printe dokument ud så det bliver lavet om til en simpel .txt fil i en folder som bliver lavet
printer = Printer()

while True:
    print("\nPrinter Options:")
    print("1. Power On")
    print("2. Power Off")
    print("3. Check Power Status")
    print("4. Load Paper")
    print("5. Current Paper Count")
    print("6. Print document")
    print("7. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '1':
        printer.power_on()
    elif choice == '2':
        printer.power_off()
    elif choice == '3':
        if printer.powered_on:
            print("The printer is powered on.")
        else:
            print("The printer is powered off.")
    elif choice == '4':
        count = int(input("Enter the number of sheets to load: "))
        printer.load_paper(count)
    elif choice == '5':
        print(f"Current paper count: {printer.paper_tray.paper_count}/{printer.paper_tray.capacity}")
    elif choice == '6':
        document = input("Enter the document to print: ")
        printer.print_document(document)
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")