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
First of all I took a look to at the logos, them come in different forms and sizes so I tought that working with percentage of the colors would be a good idea. Also similar logos had the same colors or the same shapes so I decided to work with colors and percentage but as different criteria. Many times in the logo appears the name of the company and I decided to read as mush as I can that letters. Like that I got three citeria for clasification and if two logos check at least 2, I consider them similar.
