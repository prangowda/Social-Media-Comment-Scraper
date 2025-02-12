
# **📌 Social Media Comment Scraper**  

## **🔍 Overview**  
This tool extracts **comments from public Twitter (X) posts** using **Selenium**. The extracted comments are saved in a **CSV file** for easy analysis.  

---

## **📜 Features**  
✅ **Scrapes public comments** from a given Twitter (X) post  
✅ **Automatically scrolls** to load more comments  
✅ **Saves data** in a CSV file  
✅ **Uses Selenium for automation**  

---

## **🚀 Installation**  

### **1️⃣ Install Dependencies**  
```sh
pip install selenium pandas
```

### **2️⃣ Download ChromeDriver**  
Download **ChromeDriver** (matching your Chrome version) from:  
🔗 [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)  

Place it in the project folder and update the **chromedriver.exe** path in the script if necessary.

---

## **💻 Usage**  
### **1️⃣ Edit the Python script**  
- Open `social_scraper.py`  
- Replace `post_url` with the **Twitter (X) post URL**  
- Ensure **ChromeDriver** is installed  

### **2️⃣ Run the script**  
```sh
python social_scraper.py
```

### **3️⃣ View extracted comments**  
The comments will be saved in `comments.csv` in the same directory.

---

## **📂 Example Output (`comments.csv`)**
| Comments |
|----------|
| "Elon, this is amazing!" |
| "What do you think about AI?" |
| "SpaceX launch was epic!" |

---

## **⚠ Limitations & Ethics**  
⚠ **Works only for public Twitter/X posts.**  
⚠ **Scraping private data is against Twitter’s policy.**  
⚠ **For large-scale scraping, use official APIs.**  

---

## **🔧 Future Enhancements**  
✅ Support for **Facebook, Instagram, and Reddit**  
✅ **Login automation** for scraping user-specific content  
✅ **AI-based sentiment analysis** of comments  

---

### **📌 Author: *Pranam KG(prangowda)*  
