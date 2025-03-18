import cv2
import numpy as np
import pytesseract
import os
import shutil

class Image:
    def __init__(self, colors, percent, letter, name):
        self.colors = colors
        self.percent = percent
        self.letters = letter
        self.name = name

    def __str__(self):
        return f'Image "{self.name}" has colors {self.colors} with percentages {self.percent} and contains the letters: "{self.letters}"'
    
    def percentage_matches(self, list1, list2):
        if len(list1) != len(list2):
            return False 
        
        list1_sorted = sorted(list1)  
        list2_sorted = sorted(list2)
        
        for el1, el2 in zip(list1_sorted, list2_sorted):
            if not (el1 - 5 <= el2 <= el1 + 5):  
                return False 
        
        return True 
    
    def letter_matches(self, list1, list2):
        for el1 in list1:
            for el2 in list2:
                if el1 == el2:
                    return True
        return False

    def equal(self, obj):
        count = 0
        if set(self.colors) == set(obj.colors):
            count = count + 1
        if self.percentage_matches(self.percent, obj.percent):
            count = count + 1
        if self.letter_matches(self.letters, obj.letters):
            count = count + 1
        if count >= 2:
            return True
        return False
    
COLOR_RANGES = {
    "black":   [(0, 0, 0), (180, 255, 50)],
    "white":   [(0, 0, 200), (180, 50, 255)],
    "gray":    [(0, 0, 50), (180, 50, 200)],
    "red":     [(0, 100, 100), (10, 255, 255)],
    "red2":    [(170, 100, 100), (180, 255, 255)],  # Red has two ranges
    "orange":  [(11, 100, 100), (25, 255, 255)],
    "yellow":  [(26, 100, 100), (35, 255, 255)],
    "green":   [(36, 100, 100), (85, 255, 255)],
    "blue":    [(86, 100, 100), (130, 255, 255)],
    "purple":  [(131, 50, 50), (160, 255, 255)],
    "brown":   [(10, 100, 20), (20, 255, 200)],
    "pink":    [(161, 50, 50), (170, 255, 255)]
}

# Compute color percentages
def compute_color_percentage(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    total_pixels = image.shape[0] * image.shape[1]
    
    color_percentages = []
    
    for color, (lower, upper) in COLOR_RANGES.items():
        lower_bound = np.array(lower, dtype=np.uint8)
        upper_bound = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        
        # Handle red separately (sum both ranges)
        if color == "red":
            lower2, upper2 = COLOR_RANGES["red2"]
            lower_bound2 = np.array(lower2, dtype=np.uint8)
            upper_bound2 = np.array(upper2, dtype=np.uint8)
            mask += cv2.inRange(hsv_image, lower_bound2, upper_bound2)

        color_pixels = np.count_nonzero(mask)
        percentage = (color_pixels / total_pixels) * 100
        if color != "red2":
            if percentage > 5:
                color_percentages.append([round(percentage,2), color])

    return color_percentages

def letters(image):
    pytesseract.pytesseract.tesseract_cmd = r"D:/logos/install_tesseract/tesseract.exe" 

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    extracted_text = pytesseract.image_to_string(gray_image)
    words_list = []
    words_list = extracted_text.split()

    return words_list

# Main execution
folder_path = "D:/logos/logo_image"
logos = []

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".png"):  # Filter image files
        file_path = os.path.join(folder_path, filename)
        
        image = cv2.imread(file_path)
        if image is not None:
            colors = []
            percents = []
            color_and_percents = compute_color_percentage(image)

            for el in color_and_percents:
                color = el[1]
                colors.append(color)
                per = el[0]
                percents.append(per)

            lett = letters(image)

            logo_obj = Image(colors, percents, lett, filename)
            logos.append(logo_obj)

        else:
            print(f"Error loading {filename}")

final_list = []
logos_copy = logos[:]  

while logos_copy:
    logo1 = logos_copy.pop(0)  
    new_list = [logo1] 

    for logo2 in logos_copy[:]:  
        if logo1.equal(logo2):
            logos_copy.remove(logo2)  
            new_list.append(logo2)

    final_list.append(new_list)

for el in final_list:
    print("Categorie:")
    for el1 in el:
        print(el1) 

base_dir = "D:/logos/final_results"
for idx, category in enumerate(final_list):
    category_folder = os.path.join(base_dir, f"Category_{idx+1}")
    os.makedirs(category_folder, exist_ok=True) 

    for logo in category:
        source_path = os.path.join("D:/logos/logo_image", logo.name)  
        destination_path = os.path.join(category_folder, logo.name)  
        
        if os.path.exists(source_path):  
            shutil.copy(source_path, destination_path)  
        else:
            print(f"File not found: {source_path}")