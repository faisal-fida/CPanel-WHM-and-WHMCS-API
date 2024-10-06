# CPanel and WHM API Project

## Overview

The CPanel and WHM API project is designed to streamline interactions with WHM and WHMCS systems using Python. This project includes functionalities to manage server packages, retrieve package information, and interact with WHMCS for product details. 

## Key Features

- **Package Management**: Retrieve and save details about various server packages.
- **WHMCS Integration**: Interact with the WHMCS API to fetch product information.
- **Configuration Handling**: Load and manage environment variables for secure and flexible configurations.

## Setup

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/faisal-fida/CPanel-and-WHM-API.git
   cd CPanel-and-WHM-API
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed. Then, install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   Create a `.env` file in the root directory and add the necessary environment variables:
   ```env
   WHMCS_SECRET=your_whmcs_secret
   WHMCS_IDENTIFIER=your_whmcs_identifier
   WHM_AUTH_HEADERS=your_whm_auth_headers
   WHM_SERVER_URL=your_whm_server_url
   ```

4. **Run the Main Script**:
   ```sh
   python main.py
   ```

## Complexities

- **API Integration**: Managing multiple APIs (WHM and WHMCS) with different authentication mechanisms and endpoints.
- **Data Handling**: Normalizing and processing data from APIs to a structured format (CSV) for further analysis.
- **Environment Management**: Securely managing sensitive information like API keys using environment variables.

## Solutions

- **Modular Code Structure**: Divided functionalities into separate handler files (`variable_handler.py`, `whm_handler.py`, `whmcs_handler.py`) to enhance code readability and maintainability.
- **Error Handling**: Implemented robust error handling mechanisms to manage API request failures and other potential issues.
- **Data Normalization**: Used `pandas` to normalize JSON responses and save them into structured CSV files.

## Challenges

- **API Rate Limits**: Encountered rate limits from the APIs, which required implementing retry mechanisms and optimizing API calls.
- **Data Consistency**: Ensuring data consistency and accuracy while fetching and processing data from multiple sources.
- **Security**: Managing and securing environment variables to prevent unauthorized access.
