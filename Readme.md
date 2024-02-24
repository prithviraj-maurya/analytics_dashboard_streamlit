# Streamlit Data Analytics Dashboard

This Streamlit app allows users to upload a CSV or Excel file and generates a dashboard with various analytics plots based on the data columns.

Streamlit app link: https://analytics-dashboard-drag-drop.streamlit.app

## Features

- **Upload File**: Users can upload a CSV or Excel file containing their data.
- **Dashboard**: The app generates plots based on the type of data in each column:
  - Categorical Data: Bar plot
  - Numerical Data: Box plot
  - Text Data: Word cloud

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/streamlit-data-analytics-dashboard.git
   ```

2. Install the required packages:

   ```bash
   pip install streamlit pandas matplotlib wordcloud openpyxl
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser at `http://localhost:8501`.

## Usage

1. Upload your CSV or Excel file using the sidebar.
2. Explore the dashboard with different plots for each column in your dataset.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can place this README.md file in the root directory of your project repository. Feel free to modify it to fit your project's specific details and requirements.
