# CargoWise XML Uploader - CSV to Native XML Converter

This project provides a script to convert contact information from CSV files into CargoWise's Native XML format. The generated XML file can be uploaded directly into CargoWise for seamless data integration. This script is part of a larger project to automate information uploads into CargoWise using their native XML schema.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Configuration](#configuration)
- [Features and Assumptions](#features-and-assumptions)
- [Upcoming Features](#upcoming-features)
- [License](#license)

## Overview

The current script (`CSVtoNativeXML.py`) reads contact information from a CSV file (`contactList.csv`), structures it according to CargoWise's Native XML schema, and saves it as `output.xml`. The XML structure is set to include organization details, contact information, and branch control codes to support upload and data integration with CargoWise.

## Requirements

- Python 3.x
- No additional libraries are required, as the script uses Python's built-in `csv` and `xml.etree.ElementTree` libraries.

## Usage

1. **Prepare the CSV file**:
   - Ensure your CSV file (`contactList.csv`) includes the following columns:
     - `Organisation Code`
     - `Job Category`
     - `Controlling Branch`
     - `Contact Name`
     - `Job Title`
     - `PhoneWork`
     - `PhoneMobile`
     - `Email`
   - Place `contactList.csv` in the same directory as the script.

2. **Run the Script**:
   - Execute the script by running:
     ```bash
     python CSVtoNativeXML.py
     ```
   - When prompted, enter the three-digit company code. This code will be used as the `GlbCompany` code in the XML structure.
   - The script will read `contactList.csv`, convert the data into the required XML format, and save the output as `output.xml` in the same directory.

3. **Check the Output**:
   - Once the script finishes, open `output.xml` to verify the XML structure and data.

### Example Directory Structure

```plaintext
your_project_folder/
├── contactList.csv
├── CSVtoNativeXML.py
└── output.xml
