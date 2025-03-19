# Logos Categorization Project  
_A Python script for downloading, analyzing and categorizing logos based on color composition and text recognition._

## 📌 Overview  
This project is based on two python scripts: population.py and calssification.py
It downloads (population.py) and processes (classification.py) a collection of logo images, extracts key features (dominant colors, color percentages, and detected text), and groups similar logos into categories.
Input: logos.snappy.parquet - file containing the names of the logos which will be downloaded and then processed
Output: Categories with similar logos -> one folder for each category.

## ✨ Features  
- 🐍 population.py
  - ✅ downloads images logo using Clearbit Logo API
  - ✅ store all the images in a specifc folder
  - ⚙️ asummes that all registration from .parquet file are domain names
  - ⚙️ constructs a request URL for each domain using Clearbit’s API.
  - ⚙️ if the API response is 200 (OK), downloads and saves the logo image.
  - 🔨 success rate: ~66-67% of logos successfully downloaded.
- 🐍 classification.py
  - ✅ Extracts dominant colors and their percentages from images (⚙️ HSV convertion) 
  - ✅ Detects text from logos using OCR (⚙️ Tesseract)  
  - ✅ Compares images based on:  
    - ⚙️ Color similarity (within a defined tolerance)  
    - ⚙️ Text matches  
    - ⚙️ Percentage difference in colors (within a defined tolerance)
  - ✅ Groups similar logos into categorized folders

## 🧠 The ideas:
First, I analyzed the logos and noticed that they come in various shapes and sizes. I thought that using the percentage of colors in each logo would be a good approach. Additionally, similar logos often shared the same colors or shapes, so I decided to consider both color composition and percentage as separate criteria.
Many logos also contain the company name, so I aimed to extract as many letters as possible from the text. This gave me three classification criteria: color composition, color percentage, and text recognition. If two logos matched in at least two of these criteria, I considered them similar.
I initially thought about using the company name as an additional criterion, but it felt like cheating, so I abandoned that idea.

## 🚀 Getting Started
❗ The repository reflects the state after code execution. Before running the code, delete the contents of the logo_image and final_results folders.
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pandas, requests, urllib, pillow, tesseract-ocr  
<p> In the classification.py edit the path for tesseract.exe acording to your environment. </p>

1. Open cmd in the folder you pulled the code and aditional files
2. execute "python population.py" to get all the logos in a file
3. execute "python classification.py" to get them classified


