README.md

# Cake Shop

Welcome to the **Cake Shop** project! This Python application provides a simple system for managing cake shop orders, inventory, customer data, and related operations.

## Features

- **Manage Cake Orders**: Allows users to create orders and add cakes to them.
- **Cake Information**: Defines cakes with details like name, price, ingredients, current stock, and potential discounts.
- **Customer Management**: Manages basic customer information and their order history.
- **Inventory Tracking (Basic)**: Cakes have a `stock` attribute to represent availability. (Note: The current example in `main.py` does not demonstrate dynamic stock deduction upon ordering).
- **Invoice Generation (PDF)**: Generates PDF invoices for customer orders.
- **Sales Data Export (Excel)**: Exports example sales data to an `.xlsx` file.

## Technologies Used

- **Python**: Core programming language.
- **Pipenv**: For managing virtual environments and dependencies.
- **fpdf**: For generating PDF invoices.
- **openpyxl**: For exporting data to Excel files.

## Installation

### Prerequisites

- Python 3.13 (as specified in `Pipfile`)
- pip
- pipenv

### Steps to Install

1. Clone this repository (if you haven't already):
   ```bash
   git clone https://example.com/your-repo-url.git # Replace with the actual repository URL
   cd your-repo-url # Navigate into the cloned project directory
   ```
   If you are working with a local copy that is not a git repository, simply navigate to your project's root directory (the one containing the `Pipfile` and the `Cake Shop OOP` subdirectory).

2. Install dependencies using Pipenv:
   Ensure you are in the project's root directory (where the `Pipfile` is located).
   This command will create a virtual environment if one doesn't exist and install all necessary packages listed in the `Pipfile`.
   ```bash
   pipenv install
   ```

Usage

To run the demonstration script, ensure you are in the project's root directory (the one containing the `Pipfile` and the `Cake Shop OOP` subdirectory), then execute the following command:

```bash
pipenv run python "Cake Shop OOP/main.py"
```

This script will:
- Initialize a cake shop with a sample inventory.
- Display the available cakes.
- Simulate a customer placing an order.
- Generate a PDF invoice for the order (saved as `order_invoice.pdf` in the project root).
- Export sample cake sales data to an Excel file (saved as `cake_sales.xlsx` in the project root).

