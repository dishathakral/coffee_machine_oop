# coffee_machine_oop
A command-line Coffee Machine program written in Python using Object-Oriented Programming (OOP) principles. This program simulates a coffee vending machine where users can select coffee types, process payments, and check available resources.

🚀 How It Works

The user selects a coffee type (espresso, latte, or cappuccino).
The machine checks if there are enough ingredients to make the coffee.
If sufficient resources are available, the user is prompted to insert coins.
If the inserted amount is sufficient, the coffee is dispensed, and change is returned if necessary.
The user can type "report" to view the remaining resources or "off" to turn off the machine.

🛠️ Setup & Run

Make sure you have Python installed, then clone the repository and run the script:
git clone https://github.com/dishathakral/coffee_machine_oop.git
cd coffee_machine_oop
python main.py

📂 Project Structure

coffee_machine_oop/
│── menu.py            # Manages the coffee menu
│── coffee_maker.py    # Handles coffee-making and resource management
│── money_machine.py   # Processes payment transactions
│── main.py            # Main program to run the coffee machine
│── README.md          # Project documentation
└── .gitignore         # Ignores unnecessary files
