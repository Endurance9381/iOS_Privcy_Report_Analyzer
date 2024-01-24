# iOS Privacy Report Analyzer

## Overview

The iOS Privacy Report Analyzer is a simple Python script designed to allow users to explore the application privacy report natively generated by iOS. This tool allows users to upload an iOS App privacy report file and search for specific keys within the JSON data. Common use cases include identifying domains and IP addresses that an app has connected to.

## Key Features

- **Comprehensive Insights:** Uncover a detailed list of IP addresses and domains associated with connections made by iOS apps.
- **Threat Hunting:** Use this tool to enhance threat detection capabilities and identify potential security vulnerabilities or compromises.
- **Community Collaboration:** Feel free to fork the project and contribute additional functionalities to further empower the iOS Privacy Report Analyzer.


### Obtaining the App Privacy Report

1. **Open Settings:**
   - Navigate to the "Settings" app on your iOS device.

2. **Privacy & Security:**
   - Tap on "Privacy & Security" to access privacy settings.

3. **App Privacy Report:**
   - Choose "App Privacy Report" to view an overview of app activities.

4. **Share and Save:**
   - Tap the "Share" button (usually at the top-right).
   - Save the report, choosing an option like "Save to Files."

5. **Transfer to Computer:**
   - Use iCloud Drive, AirDrop, or email to transfer the saved report to your computer.


## How to Use

1. Clone the repository to your local machine.
2. Run the script and provide the absolute path to the iOS App privacy report file when prompted.
3. Enter the key in JSON you want to search for.
4. View the results, including informative messages about the location of the key in the file.

## Example Output (Using the "domain" Key)

After running the iOS Privacy Report Analyzer and providing the "domain" key, you can expect to see all domains and IP addresses that have connected to the iPhone.


## Getting Started

```bash
# Clone the repository
git clone https://github.com/Endurance9381/iOS_Privcy_Report_Analyzer/

# Navigate to the project directory
cd iOS-Privacy-Report-Analyzer

# Run the script
python ios_privacy_analyzer.py


