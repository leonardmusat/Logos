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
- 🐍 classification.py
  - ✅ Extracts dominant colors and their percentages from images  
  - ✅ Detects text from logos using OCR (Tesseract)  
  - ✅ Compares images based on:  
    - Color similarity (within a defined tolerance)  
    - Text matches  
    - Percentage difference in colors (within a defined tolerance)
  - ✅ Groups similar logos into categorized folders

## ⚙️ How It Works  
1. Population.py: Assumtion: every registration from the .parquet file represents the domain of the specifc company.
- For every line of the .parquet file a specific url is built wehere a request of type get is applied, if the request send back "200" in the next step the logo is downloaded.
- Logos Downloaded: 66-67%
2. Classification.py
- Loads images from the folder they were downloaded   
- Compares logos based on:  
   - 🎨 Color similarity (within a defined tolerance) - converting images to a HSV 
   - 🔠 Text matches - using Tesseract OCR
   - 📊 Percentage difference in colors (within a defined tolerance) - converting images to a HSV
- Groups similar logos into separate folders

## 🧠 The ideas:
