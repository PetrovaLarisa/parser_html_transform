# JSON Data Processor
## Description

This program processes JSON data to clean and extract definitions
and sub-definitions from HTML content. The input data is expected to be in a
specific format, and the output is saved as a structured JSON file.

## Table of Contents


- [Usage](#usage)
- [Input Format](#input-format)
- [Output Format](#output-format)
- [Explanation of the Program](#explanation-of-the-program)


## Usage

1. Ensure your input file is named `UnitTestDataLarger.json` and is placed in the same directory as the script.
2. Run the script:
    ```sh
    python script.py
    ```
3. The output will be saved to `Outcome1.json` in the same directory.

## Input Format

The input JSON file `UnitTestDataLarger.json` should have the following structure:

```json
{
    "DATA": {
        "A": [
            {
                "title": "Term1",
                "body": "<html_content>"
            },
            ...
        ]
    }
}
```

## Output Format
The output JSON file Outcome1.json will have the following structure:
 ```sh
[
    {
        "term": "Term1",
        "definition": "Main definition of Term1",
        "sub_definitions": [
            {
                "term": "Subterm1",
                "definition": "Definition of Subterm1",
                "sub_definitions": [
                    {
                        "definition": "Sub-definition of Subterm1"
                    },
                    ...
                ]
            },
            ...
        ]
    },
    ...
]
```
### Explanation of the Program

The program performs the following steps:

1. **Import necessary libraries**: `json`, `re`, and `BeautifulSoup` from `bs4`.
2. **Define the `clean_beauty` function**: This function cleans HTML content using BeautifulSoup and extracts text.
3. **Load input JSON data**: The input JSON data is loaded from `UnitTestDataLarger.json`.
4. **Initialize output list**: An empty list `output` is initialized to store the processed data.
5. **Process each item in the JSON data**: The program iterates through each item in the JSON data and processes the HTML content in the `body` field to extract definitions and sub-definitions.
6. **Save the output**: The processed data is saved to `Outcome1.json`.