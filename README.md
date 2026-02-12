📚 Web Scraping Books Project
📌 Project Overview

This project demonstrates web scraping using Python to extract book details from the website Books to Scrape.

The extracted data includes book titles, prices, and ratings from multiple pages and stores them in a structured CSV file for further analysis.

This project showcases skills in:

Web scraping

HTML parsing

Data extraction

Data storage using CSV

Basic data handling using Pandas

🌐 Website Used

Books to Scrape
🔗 https://books.toscrape.com

This website is specifically designed for practicing web scraping and allows safe and ethical data extraction.

🎯 Project Objectives

Extract book data from multiple pages

Parse HTML content using BeautifulSoup

Store structured data using Pandas

Generate a CSV dataset for analysis

Practice real-world data collection techniques

🛠 Technologies & Libraries Used
🔹 Programming Language

Python 3.12

🔹 Libraries

requests – To send HTTP requests to the website

beautifulsoup4 – To parse and extract HTML data

pandas – To structure and save data into CSV format

📊 Data Extracted

The following details were extracted from the first 5 pages:

📘 Book Title

💰 Book Price

⭐ Book Rating

Total books scraped: 100 (5 pages × 20 books each)

🧠 How It Works

The script sends a request to the website.

The HTML content is parsed using BeautifulSoup.

Each book container is identified using its HTML tag and class.

Required data (title, price, rating) is extracted.

Data is stored in lists.

A Pandas DataFrame is created.

The dataset is saved as books_data.csv.

📁 Project Structure
web_scraping_project/
│
├── scraper.py          # Main scraping script
├── books_data.csv      # Output dataset
└── README.md           # Project documentation

▶ How To Run The Project
Step 1: Clone the Repository
git clone https://github.com/yourusername/web-scraping-books-project.git

Step 2: Navigate to Project Folder
cd web-scraping-books-project

Step 3: Install Required Libraries
pip install requests beautifulsoup4 pandas

Step 4: Run the Script
python scraper.py


After execution, a file named books_data.csv will be generated automatically.

📸 Sample Output (CSV Format)
Title	Price	Rating
A Light in the Attic	£51.77	Three
Tipping the Velvet	£53.74	One
Sharp Objects	£47.82	Four
🚀 Future Improvements

Convert price to numeric format

Convert rating text to numeric scale (1–5)

Add data visualization using Matplotlib

Scrape all available pages

Store data in a database instead of CSV

📌 Skills Demonstrated

Web Scraping

HTML Inspection using Developer Tools

Data Cleaning Basics

Python Programming

Data Storage & Handling

👩‍💻 Author

Saranya S