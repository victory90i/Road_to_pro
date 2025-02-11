"""
Python Packages and File Handling Projects
----------------------------------------
A practical guide with exercises on installing and using popular Python packages.
Each exercise includes installation instructions and sample projects.

Exercise 1: Data Analysis with PrettyTable
----------------------------------------
Installation Guide:
```bash
pip install prettytable
```

Project: Student Performance Dashboard
Create a formatted table showing student performance data.

Requirements:
1. Read student data from a CSV file:
   - Name, Math, Science, English, History
2. Calculate averages per subject
3. Format data in a pretty table
4. Add color highlighting for top performers

Example Code:
```python
from prettytable import PrettyTable
import csv

def create_performance_table():
    table = PrettyTable()
    table.field_names = ["Name", "Math", "Science", "English", "History", "Average"]
    
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            scores = [int(row[subject]) for subject in ["Math", "Science", "English", "History"]]
            avg = sum(scores) / len(scores)
            table.add_row([row["Name"]] + scores + [f"{avg:.2f}"])
    
    print(table)

# Example students.csv content:
# Name,Math,Science,English,History
# John,85,92,78,88
# Sarah,92,88,95,85
"""

"""
Exercise 2: Interactive Web Apps with Gradio
-----------------------------------------
Installation Guide:
```bash
pip install gradio
```

Project: Image Filter Application
Create a web interface for applying filters to images.

Requirements:
1. Build interface with:
   - Image input
   - Filter selection dropdown
   - Processed image output
2. Implement basic filters:
   - Grayscale
   - Blur
   - Brightness adjustment

Example Code:
```python
import gradio as gr
import numpy as np
from PIL import Image, ImageEnhance

def apply_filter(image, filter_type):
    img = Image.fromarray(image)
    if filter_type == "Grayscale":
        return np.array(img.convert('L'))
    elif filter_type == "Blur":
        # Add blur implementation
        pass
    return np.array(img)

interface = gr.Interface(
    fn=apply_filter,
    inputs=[gr.Image(), gr.Dropdown(["Grayscale", "Blur", "Bright"])],
    outputs=gr.Image()
)
interface.launch()
"""

"""
Exercise 3: Data Visualization with Streamlit
------------------------------------------
Installation Guide:
```bash
pip install streamlit
```

Project: Sales Dashboard
Create an interactive dashboard for sales data visualization.

Requirements:
1. Load sales data from CSV
2. Create interactive charts:
   - Monthly sales trend
   - Product category breakdown
   - Regional comparison

Example Code:
```python
import streamlit as st
import pandas as pd
import plotly.express as px

def create_dashboard():
    st.title("Sales Dashboard")
    
    # Load data
    data = pd.read_csv('sales.csv')
    
    # Monthly trend
    st.subheader("Monthly Sales Trend")
    monthly_sales = data.groupby('Month')['Sales'].sum()
    st.line_chart(monthly_sales)
    
    # Add more visualizations...

# Run with: streamlit run dashboard.py
"""

"""
Exercise 4: Data Processing with NumPy
-----------------------------------
Installation Guide:
```bash
pip install numpy
```

Project: Weather Data Analysis
Analyze temperature data using NumPy arrays.

Requirements:
1. Load temperature readings from file
2. Calculate:
   - Daily averages
   - Temperature variations
   - Extreme values
3. Generate statistical report

Example Code:
```python
import numpy as np

def analyze_temperatures():
    # Load data from file
    temps = np.loadtxt('temperatures.txt')
    
    # Calculate statistics
    daily_avg = np.mean(temps, axis=1)
    temp_range = np.ptp(temps, axis=1)
    extremes = {
        'max': np.max(temps),
        'min': np.min(temps)
    }
    
    return daily_avg, temp_range, extremes
"""

"""
Exercise 5: Data Analysis with Pandas
----------------------------------
Installation Guide:
```bash
pip install pandas
```

Project: E-commerce Data Analysis
Analyze customer purchase patterns.

Requirements:
1. Read purchase history from CSV
2. Analyze:
   - Customer spending patterns
   - Popular products
   - Peak shopping times
3. Generate insights report

Example Code:
```python
import pandas as pd

def analyze_purchases():
    # Read data
    df = pd.read_csv('purchases.csv')
    
    # Customer analysis
    customer_spend = df.groupby('customer_id')['amount'].sum()
    popular_products = df['product'].value_counts().head()
    
    # Time analysis
    df['date'] = pd.to_datetime(df['date'])
    hourly_sales = df.groupby(df['date'].dt.hour)['amount'].sum()
    
    return customer_spend, popular_products, hourly_sales
"""

"""
Exercise 6: File Operations
-------------------------
Project: Log File Analyzer
Create a system to process and analyze log files.

Requirements:
1. Read log files
2. Parse different log formats
3. Generate summary reports
4. Archive processed files

Example Code:
```python
def analyze_logs():
    with open('app.log', 'r') as log_file:
        # Process logs
        logs = log_file.readlines()
        
        # Parse each line
        for line in logs:
            # Extract timestamp, level, message
            parts = line.split(' - ')
            
            # Process based on log level
            if 'ERROR' in line:
                handle_error(parts)
            elif 'WARNING' in line:
                handle_warning(parts)
    
    # Generate report
    with open('report.txt', 'w') as report:
        report.write(summary)
"""

"""
Exercise 7: Combined Project - Data Pipeline
-----------------------------------------
Project: Create a complete data processing pipeline using multiple packages.

Requirements:
1. Read raw data files using Pandas
2. Process data using NumPy
3. Create visualizations with Streamlit
4. Generate formatted reports with PrettyTable
5. Build interactive interface with Gradio

Example Structure:
```python
# Import required packages
import pandas as pd
import numpy as np
import streamlit as st
from prettytable import PrettyTable
import gradio as gr

class DataPipeline:
    def __init__(self):
        self.data = None
        
    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)
        
    def process_data(self):
        # NumPy calculations
        pass
        
    def create_visualization(self):
        # Streamlit dashboard
        pass
        
    def generate_report(self):
        # PrettyTable report
        pass
        
    def launch_interface(self):
        # Gradio interface
        pass

# Usage
pipeline = DataPipeline()
pipeline.load_data('data.csv')
pipeline.process_data()
pipeline.create_visualization()
```

Installation Tips:
-----------------
1. Use virtual environments:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\\Scripts\\activate
   ```

2. Install all packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Common issues:
   - Ensure pip is updated: pip install --upgrade pip
   - Check Python version compatibility
   - Install required system dependencies

4. Package management:
   - Create requirements.txt: pip freeze > requirements.txt
   - Install from requirements: pip install -r requirements.txt
"""