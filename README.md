# 📊 Simple Retail Sales Analysis

## 🎯 What This Project Does
Learn basic data analysis using pandas and matplotlib. We'll clean sales data and create simple charts to find business insights.

**Perfect for beginners** who want to practice:
- Loading data from CSV files
- Cleaning messy real-world data
- Calculating business metrics
- Creating visualizations
- Generating insights

## 🎓 Skills You'll Learn
- `pd.read_csv()` - Load data from files
- `.head()` and `.info()` - Explore your data
- `.isnull().sum()` - Find missing values
- `.dropna()` - Remove missing data
- Simple filtering: `df[df['column'] > 0]`
- Basic math: `df['A'] * df['B']`
- `.groupby().sum()` - Group data by categories
- `.sort_values()` - Sort your results
- `plt.bar()` and `plt.hist()` - Make simple charts
- `.to_csv()` - Save your results

## 🚀 Quick Start

### Step 1: Get the Project
```bash
git clone https://github.com/craftedcode45/Simple-Retail-Analysis.git
cd Simple-Retail-Analysis
```

### Step 2: Install Packages
```bash
pip install -r requirements.txt
```

### Step 3: Create Sample Data
```bash
python create_sample_data.py
```

### Step 4: Start Analysis
```bash
jupyter notebook simple_retail_analysis.ipynb
```

## 📁 What's Inside
```
Simple-Retail-Analysis/
├── simple_retail_analysis.ipynb   # Main analysis (START HERE)
├── create_sample_data.py          # Creates practice data
├── requirements.txt               # Packages you need
├── README.md                      # This guide
├── sales_data.csv                 # Sample data (created by script)
├── clean_sales_data.csv          # Clean data (created by analysis)
└── summary.csv                   # Key results (created by analysis)
```

## 📊 What You'll Discover
After running the analysis, you'll find:
- **Total Sales**: How much money was made
- **Top Countries**: Which countries buy the most
- **Best Products**: What sells the best
- **Customer Insights**: How much people spend on average
- **Visual Charts**: Easy-to-read graphs showing patterns

## 🎨 Charts You'll Create
1. **Country Sales Bar Chart** - See which countries generate most revenue
2. **Order Value Histogram** - Understand how much customers typically spend
3. **Top Products Chart** - Identify best-selling items

## 🧹 Data Cleaning You'll Learn
- Remove rows with missing customer information
- Filter out invalid prices (zero or negative)
- Create new calculated columns
- Handle real-world data problems

## 💡 Sample Results
```
✅ Analysis Complete!
Key findings:
- Total sales: £89,234.56
- Top country: UK
- Average customer spends: £156.78
```

## 🎓 Perfect For
- **Complete Beginners**: Just learned pandas basics
- **Students**: Need a portfolio project
- **Career Switchers**: Building data analysis skills
- **Self-Learners**: Want hands-on practice

## 🔍 What Makes This Beginner-Friendly?
- ✅ Only uses basic pandas operations
- ✅ Step-by-step explanations
- ✅ No advanced techniques
- ✅ Clear comments in code
- ✅ Sample data included
- ✅ Works on any computer

## 🚫 What's NOT in This Project
- No complex datetime operations
- No advanced statistical methods
- No machine learning
- No complex visualizations
- No database connections

## 🔜 Next Steps
After completing this project, you'll be ready for:
- **Project #2**: API data collection
- SQL database operations
- Advanced visualizations
- Time series analysis
- Machine learning basics

## ❓ Need Help?
- Check that all files are in the same folder
- Make sure you ran `create_sample_data.py` first
- Ensure all packages are installed
- Run cells in order from top to bottom

## 👨‍💻 Author
**CraftedCoder** - [GitHub Profile](https://github.com/craftedcode45)

*Part of the 12-Week Data Analytics Portfolio Series*

## 📄 License
This project is open source and available under MIT License. Feel free to use for learning!

---

**⭐ If this helped you learn, please star the repository!**