Flask M-Pesa Integration
This project demonstrates how to integrate M-Pesa functionality into a Flask web application. The application allows users to initiate M-Pesa STK Push transactions using a simple web interface.

Features
STK Push Integration: Enables users to initiate M-Pesa transactions directly from the web application.
Callback Handling: Handles M-Pesa callback responses to track transaction statuses.
Template Rendering: Utilizes Flask's template rendering to provide dynamic HTML content.
Responsive Design: Provides a user-friendly interface using HTML, JavaScript, and CSS.
Requirements
Python 3.x
Flask
Requests library for Python
M-Pesa Developer Account (Sandbox environment for testing)
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/jumla-online/flask-mpesa-integration.git
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure M-Pesa Credentials:

Obtain M-Pesa API credentials (consumer key, consumer secret, etc.) from the Safaricom Developer Portal.
Update the access_token.py and lipana_mpesa_password.py files with your credentials.
Run the Flask application:

bash
Copy code
python app.py
Access the application in your web browser at http://localhost:5000.

Usage
Access the web interface.
Enter your name and phone number.
Click on the "Initiate Payment" button.
Follow the prompts on your phone to complete the M-Pesa transaction.
View transaction status updates in the application.
Folder Structure
templates/: Contains HTML templates for rendering dynamic content.
static/: Stores static assets such as CSS stylesheets and JavaScript files.
app.py: Main Flask application file containing route definitions and logic.
access_token.py: Stores M-Pesa access token retrieval logic.
lipana_mpesa_password.py: Stores M-Pesa password generation logic.
README.md: This README file providing information about the project.
Contributing
Contributions are welcome! Please feel free to submit issues and pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to Safaricom for providing the M-Pesa API.
Thanks to the Flask community for the web framework.
