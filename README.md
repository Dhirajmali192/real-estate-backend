🏠 Real Estate Analysis Web App

A web-based application that analyzes real estate trends for any area using Excel dataset, Django backend, AI summary (OpenAI API), and React/HTML frontend.

🚀 Project Overview

This app allows users to enter any area name (e.g., Karad) and view:
✔ Real estate trends by year
✔ AI-generated professional summary
✔ Interactive chart visualization
✔ Table view of filtered data
✔ Option to download Excel data

🧠 Key Features
Feature	Description
🔍 Area Search	Analyze any area from Excel dataset
📊 Chart Visualization	Year-wise sales & units sold
📋 Table View	Complete detailed dataset
🤖 AI Summary	OpenAI GPT generates insights
💾 Excel Download	Export filtered data
🌐 API Tested in Postman	Fully functional backend
🧰 Tech Stack
Technology	Usage
Django (DRF)	Backend REST API
Pandas	Excel data processing
OpenAI API	AI-generated summary
React / HTML / JS	Frontend UI
Postman	API testing
Excel (.xlsx)	Dataset
📂 Project Structure
real-estate-analysis/
│
├── backend/
│   ├── chatbot/
│   │   ├── views.py
│   │   ├── urls.py
│   ├── backend/
│   │   ├── settings.py
│   │   ├── urls.py
│   ├── data/
│   │   └── real_estate.xlsx
│   └── manage.py
│
├── frontend/
│   ├── index.html / React files
│
└── README.md  <-- YOU ARE HERE

⚙️ Backend Setup (Django)
# 1. Activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install django djangorestframework pandas openai

# 3. Run Server
python manage.py runserver

🔗 API Routes
API Endpoint	Method	Description
/api/chatbot/analyze/?area=Karad	GET	Analyze area data
/api/chatbot/download/?area=Karad	GET	Download Excel file
📌 Frontend API Fetch Example
const response = await fetch(
  `https://real-estate-backend-q544.onrender.com/api/chatbot/analyze/?area=${area}`
);
const data = await response.json();
setChartData(data.chart_data);
setTableData(data.table_data);
setSummary(data.summary);

📌 Demo Screenshot (Sample)

🟩 Enter Area → Click Analyze → Output Appears

Chart	Table	AI Summary
🧪 Postman API Testing

✔ Works without frontend
✔ Use this request to test:

GET  /api/chatbot/analyze/?area=Karad

🧾 License

This project is developed for academic & learning purpose only.
Free to use & modify.

📌 Future Scope

✔ AI-based price prediction
✔ Multi-area comparison
✔ Location-based map visualization
✔ User authentication system

🙋 Developed By

Name: Dhiraj Mali
Course: MCA
Tech Stack: Django + React + OpenAI
Project Type: Real Estate Analysis Web Application

📢 Conclusion

This project successfully demonstrates data handling, AI integration, API development, frontend communication, and real-world real estate analysis.
