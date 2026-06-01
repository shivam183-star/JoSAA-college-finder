# JoSAA College Finder

A Streamlit-based dashboard that helps students explore potential college and branch options using historical JoSAA closing rank data.

## Features

* Filter colleges based on:

  * Gender
  * Category (Seat Type)
  * Quota
  * JEE Mains Rank
  * Preferred Branch
* Interactive and user-friendly interface
* View filtered results in a searchable table
* Download filtered results as CSV
* Fast loading using Streamlit caching
* Wide-screen layout for easier comparison of colleges and branches

## Dataset

The application uses historical JoSAA cutoff data stored in an Excel file (`JoSAA.xlsx`).

Before processing:

* Rows with provisional ranks (ending in `P`) are removed.
* Closing ranks are converted to numeric values for comparison.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shivam183-star/JoSAA-college-finder.git
cd JoSAA-college-finder
```

### 2. Install dependencies

```bash
pip install requirements.txt
```

### 3. Place the dataset

Ensure that the file below is present in the project directory:

```text
JoSAA.xlsx
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

## Usage

1. Select your:

   * Gender
   * Category
   * Quota

2. Enter your rank.

3. Select your branch preference.

4. The dashboard will display all college-branch combinations whose previous year closing rank is greater than your entered rank.

5. Download the filtered results using the **Download CSV** button.

## Disclaimer

⚠️ This tool is intended for informational and guidance purposes only.

The predictions are based on historical JoSAA closing rank data from previous years and should not be considered a guarantee of admission.

Actual seat allotment may vary due to factors including:

* Changes in seat matrix
* Number of applicants
* Difficulty level of examinations
* Reservation policies
* Counseling choices made by candidates
* Year-to-year cutoff fluctuations

A college or branch appearing in the results does **not guarantee admission**, and a college or branch not appearing in the results may still be obtainable in the current admission cycle.

Always refer to official JoSAA counselling information before making admission decisions.

## Tech Stack

* Python
* Pandas
* Streamlit
* OpenPyXL


# 📄 License

This project is licensed under the [MIT License](LICENSE).

---

# 👨‍💻 Author

## Shivam Singh

### Connect with Me
- [GitHub](https://github.com/shivam183-star)
- [LinkedIn](https://www.linkedin.com/in/shivam-singh-15b79a31a/)

---

# ⭐ Support

If you found this project useful:
- Give it a ⭐ on GitHub
- Share it with others
- Fork the repository

---

# 📌 Note

This project is intended for educational and portfolio purposes.
Data belongs to Joint Seat Allocation Authority
