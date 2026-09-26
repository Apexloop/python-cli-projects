# Python OOP & CLI Projects Portfolio

A collection of terminal-based Object-Oriented Programming (OOP) applications and command-line interface (CLI) tools built using Python. This repository showcases key software engineering fundamentals, including encapsulation, object composition, interactive state management, and file persistence via JSON.

---

## 🚀 Featured Projects

### 1. Vehicle Rental Management System (`rental.py`)
A CLI application for managing a rental fleet and processing vehicle bookings[cite: 1].
* **OOP Architecture:** Built using `Vehicle` and `RentalAgency` classes.
* **Core Functionality:** Tracks vehicle availability, calculates total rental costs based on duration, handles returns, and updates vehicle status dynamically.
* **Data Persistence:** Serializes fleet data and states into `vehicles.json` across sessions.

### 2. Digital Library Management System (`library.py`)
An interactive library tracking system for books and checkout states[cite: 1].
* **OOP Architecture:** Built using `Book` and `Library` classes.
* **Core Functionality:** Case-insensitive title searching, checking out/returning books, and real-time inventory updates.
* **Data Persistence:** Automatically saves and loads library state from `library.json`.

---

## 🛠️ Additional CLI Tools

* **`bank.py`**: Banking system simulation for account management and transaction handling[cite: 1].
* **`expense.py`**: Personal expense logging tool for categorizing spending[cite: 1].
* **`calculator.py`**: Command-line calculator with memory storage support[cite: 1].
* **`passsword generator.py`**: Utility for generating randomized passwords[cite: 1].

---

## 🛠️ Key Concepts & Skills Demonstrated

* **Object-Oriented Programming (OOP):** Encapsulation, object composition, constructor initialization, and method separation.
* **Data Persistence:** JSON serialization (`json.dump`, `json.load`) and object dictionary translation (`to_dict`).
* **Error Handling:** Safe file reading with `try/except` blocks and input validation loops.
* **CLI UX Design:** Infinite menu loops with formatted output and clear user prompts.

---

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Apexloop/vehicle-rental-system.git](https://github.com/Apexloop/vehicle-rental-system.git)
   cd vehicle-rental-system

   # Run the Vehicle Rental System
python rental.py

# Run the Digital Library System
python library.py

👤 Author
Muhammad Huzaifa

GitHub: @Apexloop
