# 📊 WhatsApp Chat Analyzer**
Welcome to the **WhatsApp Chat Analyzer!** This web application allows users to upload their exported WhatsApp chat data (in .txt format) to generate insightful visualizations like message frequency analysis, most active users, and word clouds.

# 📝 Project Overview
The **WhatsApp Chat Analyzer** is a Flask-based web application that processes exported WhatsApp chat data to analyze:

**Most Active Users**: Insights on which users sent the most messages.
**Word Cloud**: Visualization of frequently used words in the chat.
**Message Frequency Trends**: Graphs showing the message patterns over time.
This web application empowers users to better understand their WhatsApp communication patterns through data visualization.

## 🛠️ Technologies Used
**Python 🐍**
**Flask**
**Pandas**
**Matplotlib**
**Seaborn**
**WordCloud**
**Frontend: Streamlit**
**Data Visualization: Matplotlib and Seaborn for insights visualization**
**Deployment: Render**

## 🚀 Features
**✅ Upload Chat Data**
Users can upload their exported WhatsApp chat files (in .txt format).

**✅ View Insights**
Generate interactive visualizations such as:
Most Active Users Graph 📊
Message Frequency Trends 📈

**Word Cloud 🔤**
✅ Easy Analysis Dashboard
A simple interface to explore insights easily.

**✅ Real-Time Visualization**
Real-time insights are generated as soon as data is processed.

**📂 Installation & Setup**
To run the WhatsApp Chat Analyzer locally, follow the steps below:

---
### Steps

1. Clone the Repository
```bash
Copy code
git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```

2. Set Up a Virtual Environment
```bash
Copy code
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. Install Dependencies
```bash
Copy code
pip install -r requirements.txt
```

4. Run the Application
```bash
Copy code
python app.py
```

5. Open the App
Open a browser and go to:


https://whatsapp-chat-analyzer-v962.onrender.com
---

## 📂 Project Structure
```plaintext
Copy code
whatsapp-chat-analyzer/
├── src/
│   ├── data_processing.py
│   ├── analysis.py
│   └── visualization.py
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
Explanation of the structure
src/
```

Contains all core logic for:

Parsing the uploaded chat data.
Processing insights and data analysis.
Visualizations using Matplotlib/Seaborn.
templates/
HTML templates for rendering Flask views.

**app.py**
The entry point for the Flask web application.

**requirements.txt**
Contains all the necessary dependencies to run the project.

**🌐 Deployment**
You can deploy this project on platforms like Render, Heroku, AWS, or PythonAnywhere using the following steps:

**Render Deployment**
Create a Render account.
Link your repository to Render.
Add the following to Start Command:
bash
Copy code
streamlit run app.py
Deploy your application and visit the generated URL.

## 🧪 How to Use
**1. Upload Your Chat Data**
Export your chat from WhatsApp by going to the chat, clicking on the three dots menu, selecting More > Export Chat, and then saving it as a .txt file.
Use the application’s file upload option.
**2. Explore Insights**
After uploading:

View the Word Cloud visualization.
Check insights like Most Active Users graphs.
Analyze trends of messages over time (frequency trends).

**📊 Input Example**

**Example File Format:**
A typical WhatsApp exported chat looks like this:

yaml
Copy code
12/01/2023, 8:30 PM - John Doe: Hello
12/01/2023, 8:32 PM - Alice: Hi!
12/01/2023, 8:35 PM - John Doe: How are you doing?
12/01/2023, 8:40 PM - Alice: I’m fine, thanks!
🏆 Visualizations

**1. Most Active Users:**
A bar graph showing the most active users in the uploaded conversation.

**2. Word Cloud:**
Shows the most commonly used words in the conversation.

**3. Message Frequency Trend:**
Trends visualization over time to see peaks in message activity.

**📧 Contact Information**
For suggestions, issues, or contributions:

**Email:** your-email@example.com

**GitHub Profile:** https://github.com/DeepakChander
🤝 Contributing
Contributions to this project are welcome! If you’d like to contribute:


