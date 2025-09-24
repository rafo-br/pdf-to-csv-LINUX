# PDF to CSV Converter for Linux

A command-line Python script to extract tabular data from PDF files and save it as a single CSV file. This is an enhanced version of an existing script, adapted to be more robust and user-friendly for Linux environments.

## Key Features

-   **Command-Line Interface:** Pass the PDF file path directly as an argument in your terminal.
-   **Dependency Check:** Automatically checks if Ghostscript is installed before running.
-   **Progress Bar:** Displays a `tqdm` progress bar, which is useful for large PDF files.
-   **Robust Error Handling:** Catches common errors like missing files or problematic pages.
-   **Dynamic Output:** Automatically creates a CSV file with the same name as the input PDF.

## Requirements

### System Dependencies
-   Python 3.x
-   Ghostscript

### Python Libraries
All required Python libraries are listed in `requirements.txt`.

## Installation

Follow these steps to set up the project and its dependencies.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USER/pdf-to-csv-LINUX.git](https://github.com/YOUR_USER/pdf-to-csv-LINUX.git)
    cd pdf-to-csv-LINUX
    ```
    *(Replace `YOUR_USER` with your GitHub username)*

2.  **Install Ghostscript:**
    This script relies on Ghostscript. On Debian-based systems (like Ubuntu, Lubuntu, Mint), you can install it with:
    ```bash
    sudo apt update && sudo apt install ghostscript
    ```

3.  **Set up a Python Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Make the script executable (only needs to be done once):**
    ```bash
    chmod +x pdf-to-csv.py
    ```

2.  **Run the script:**
    Provide the path to the PDF file you want to convert as an argument.
    ```bash
    ./pdf-to-csv.py /path/to/your/file.pdf
    ```
    The output CSV file will be saved in the same directory as your PDF.
