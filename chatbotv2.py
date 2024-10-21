import random
import gradio as gr
import json
import os

responses = {
    
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm good, thank you! How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I didn't understand that. Can you please rephrase?",
    "what's your name": "I am your virtual assistant. How can I help you?",
    "who are you": "I am an AI chatbot designed to assist you with various tasks.",
    "how old are you": "I don't age, but I am always learning and improving!",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "what is your purpose": "My purpose is to assist you with tasks and provide information.",
    "can you help me": "Absolutely! What can I assist you with?",
    "thank you": "You're welcome! Feel free to ask if you need anything else.",
    "sorry": "No problem! How can I help?",
    "good morning": "Good morning! Hope you have a fantastic day ahead!",
    "good night": "Good night! Sleep well and take care.",
    "what is your favorite color": "I don't have preferences, but I think blue is calming.",
    "can you speak other languages": "Yes, I can understand and respond in many languages.",
    "what's the weather like": "I can help with that! Just tell me your location.",
    "tell me a fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs!",
    "what time is it": "I don't have real-time data, but you can check the time on your device.",
    "how do you work": "I use machine learning and natural language processing to understand and respond to your questions.",
    "are you human": "No, I am an AI, a program created to assist with various tasks.",
    "how can I learn Python": "I recommend starting with basic syntax and gradually progressing to libraries like Pandas and TensorFlow.",
    "what is machine learning": "Machine learning is a field of AI that uses algorithms to learn from and make predictions on data.",
    "what is artificial intelligence": "AI is the simulation of human intelligence processes by machines, particularly computers.",
    "do you know Python": "Yes, I can help with Python programming! What would you like to know?",
    "how can I improve my coding skills": "Practice regularly, work on projects, and study algorithms and data structures.",
    "tell me about data science": "Data science involves extracting insights from data using statistics, programming, and machine learning.",
    "what is data analysis": "Data analysis is the process of inspecting, cleaning, transforming, and modeling data to discover useful information.",
    "can you write code for me": "Yes, I can assist with writing code. What do you need help with?",
    "help me debug my code": "Sure! Share the code, and I'll help you debug it.",
    "what is a neural network": "A neural network is a series of algorithms that attempt to recognize underlying relationships in a set of data.",
    "what is deep learning": "Deep learning is a subset of machine learning that uses neural networks with many layers to analyze data.",
    "do you know TensorFlow": "Yes, I am familiar with TensorFlow. It's a popular open-source framework for machine learning and deep learning.",
    "what is PyTorch": "PyTorch is an open-source deep learning framework that's known for its flexibility and speed.",
    "can you help with SQL": "Yes, I can help with SQL queries! What do you need assistance with?",
    "what is a database": "A database is an organized collection of structured information or data, typically stored electronically.",
    "tell me about Pandas": "Pandas is a powerful Python library for data manipulation and analysis, particularly useful for handling tabular data.",
    "what is NumPy": "NumPy is a Python library used for working with arrays and matrices, and it provides a large collection of mathematical functions.",
    "what is matplotlib": "Matplotlib is a Python library for creating static, animated, and interactive visualizations.",
    "what is a chatbot": "A chatbot is an AI-powered program designed to simulate conversation with users, often for customer service or assistance.",
    "can you explain an algorithm": "Sure! Let me know which algorithm you'd like me to explain.",
    "can you help with statistics": "Yes, I can help with statistical concepts and calculations. What do you need help with?",
    "what is probability": "Probability is the measure of the likelihood that an event will occur.",
    "can you play music": "I can't play music, but I can suggest some tracks! What kind of music do you like?",
    "what is your favorite movie": "I don't have a favorite movie, but I can suggest some based on your interests!",
    "can you recommend a book": "Sure! What type of book are you looking for?",
    "do you like pizza": "I don't eat, but I know pizza is a favorite for many people!",
    "what's 2 + 2": "2 + 2 equals 4.",
    "what is 5 times 5": "5 times 5 equals 25.",
    "what is the capital of France": "The capital of France is Paris.",
    "who is the president of the USA": "The president of the USA is Joe Biden.",
    "do you know about quantum computing": "Yes, quantum computing is a field that leverages quantum mechanics to perform computations.",
    "what is blockchain": "Blockchain is a decentralized digital ledger used to record transactions across many computers.",
    "can you tell me a riddle": "Sure! Here's a riddle: What has keys but can't open locks? A piano!",
    "how do I start a project": "Start by defining your goal, breaking it down into smaller tasks, and planning out your timeline.",
    "can you help me with my homework": "I'd be happy to help! What's the subject or question?",
    "what is a resume": "A resume is a document that outlines your work experience, education, skills, and accomplishments for job applications.",
    "how do I write a cover letter": "A cover letter should highlight your qualifications, interest in the position, and why you're a good fit for the company.",
    "do you know about web development": "Yes, I can help with web development! Are you working with front-end or back-end?",
    "what is HTML": "HTML (Hypertext Markup Language) is the standard language used to create webpages and web applications.",
    "what is CSS": "CSS (Cascading Style Sheets) is used to style and layout HTML elements on a webpage.",
    "what is JavaScript": "JavaScript is a programming language used to create interactive effects within web browsers.",
    "can you help me with GitHub": "Yes, I can help with GitHub! What do you need assistance with?",
    "how are you doing": "I'm doing great, thanks for asking! How about you?",
    "good morning": "Good morning! Hope you have a wonderful day ahead.",
    "good afternoon": "Good afternoon! How’s your day going?",
    "good evening": "Good evening! I hope your day went well.",
    "good night": "Good night! Sleep tight.",
    "bye": "Goodbye! Take care and see you soon.",
    "see you later": "See you later! Have a great day!",
    "take care": "You too! Stay safe.",
    "thank you": "You're welcome! Let me know if you need anything else.",
    "thanks": "You're welcome!",
    "no problem": "No problem at all! Glad to help.",
    "sorry": "It’s okay! How can I assist you?",
    "excuse me": "Yes? How can I help?",
    "please": "Of course! What do you need?",
    "you're welcome": "I'm happy to help!",
    "can you help me": "Absolutely! What do you need help with?",
    "can you assist me": "Sure! What can I do for you?",
    "can you do that": "Yes, I can! Just let me know what you need.",
    "help me": "Of course! What do you need help with?",
    "I don't understand": "No worries, can you rephrase that?",
    "what is your name": "I am your virtual assistant. How can I help you?",
    "who are you": "I am a chatbot designed to assist with your tasks and queries.",
    "what's up": "Not much! What’s up with you?",
    "what are you doing": "I'm here to assist you! How can I help?",
    "tell me a joke": "Why don't skeletons fight each other? They don't have the guts!",
    "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs!",
    "what's your favorite color": "I don't have a favorite color, but I think blue is calming.",
    "what's your favorite food": "I don’t eat, but I know pizza is a popular favorite!",
    "what time is it": "I don’t have real-time data, but you can check the time on your device.",
    "how old are you": "I don't age, but I’m constantly learning and evolving!",
    "are you human": "No, I’m an AI designed to assist you.",
    "do you like music": "I don’t have preferences, but I can suggest some tunes for you!",
    "do you like movies": "I don’t watch movies, but I can suggest some based on your taste!",
    "can you play music": "I can't play music directly, but I can recommend some songs!",
    "can you recommend a movie": "Sure! What genre are you interested in?",
    "can you recommend a book": "Of course! What type of book do you enjoy?",
    "how's the weather": "I can’t check the weather, but you can try an app or website for the latest updates.",
    "what is the weather today": "I don’t have access to live weather data. You might want to check your local weather app.",
    "tell me the news": "I can’t provide real-time news, but you can check out the latest updates on news websites or apps.",
    "how do you work": "I use artificial intelligence and natural language processing to understand and respond to your queries.",
    "can you speak other languages": "Yes, I can assist in multiple languages! What language would you like to use?",
    "what is AI": "Artificial intelligence is the simulation of human intelligence by machines that can perform tasks like reasoning, learning, and problem-solving.",
    "what is machine learning": "Machine learning is a subset of AI that enables computers to learn from data and make decisions without being explicitly programmed.",
    "can you write code": "Yes, I can help with writing code. What programming language are you working with?",
    "do you know Python": "Yes! Python is one of my specialties. What would you like help with?",
    "what is Python": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
    "what is SQL": "SQL (Structured Query Language) is a standard language used to manage and manipulate databases.",
    "what is a database": "A database is an organized collection of data, typically stored and accessed electronically.",
    "can you help with SQL queries": "Yes! Feel free to share your query, and I'll assist you with it.",
    "what is a chatbot": "A chatbot is an AI system that can simulate conversation with users, often through text or voice.",
    "what is deep learning": "Deep learning is a subset of machine learning that uses neural networks with many layers to process and learn from large amounts of data.",
    "what is a neural network": "A neural network is a series of algorithms designed to recognize patterns in data, inspired by the human brain.",
    "what is Pandas": "Pandas is a powerful Python library used for data manipulation and analysis, particularly with structured data.",
    "what is NumPy": "NumPy is a Python library used for numerical computing, specifically with arrays and matrices.",
    "what is Matplotlib": "Matplotlib is a Python library for creating static, animated, and interactive visualizations.",
    "what is Git": "Git is a version control system that helps developers track changes in their code and collaborate with others.",
    "what is GitHub": "GitHub is a platform for hosting and sharing code, and it allows developers to collaborate using Git.",
    "how do I start learning Python": "Start by learning the basic syntax, then move on to libraries like Pandas, NumPy, and Matplotlib for data manipulation.",
    "can you help me with homework": "I'd be happy to help! What subject or question do you need assistance with?",
    "can you help with writing": "Absolutely! What are you writing? I can assist with grammar, structure, and ideas.",
    "do you understand math": "Yes! I can help with math problems, equations, and explanations. What do you need help with?",
    "how do I improve my coding skills": "Practice regularly, work on projects, and explore new coding challenges.",
    "what is an algorithm": "An algorithm is a step-by-step procedure for solving a problem or performing a task.",
    "what is data science": "Data science involves extracting insights and knowledge from structured and unstructured data using techniques from statistics, machine learning, and data analysis.",
    "can you explain statistics": "Sure! Statistics is the study of data collection, analysis, interpretation, and presentation.",
    "what is probability": "Probability is the measure of the likelihood that an event will occur.",
    "what is a resume": "A resume is a document that outlines your professional experience, skills, and education.",
    "how do I write a cover letter": "A cover letter should highlight your qualifications, explain why you're a good fit for the job, and express enthusiasm for the position.",
    "what is HTML": "HTML (Hypertext Markup Language) is used to structure content on the web.",
    "what is CSS": "CSS (Cascading Style Sheets) is used to style and layout HTML elements.",
    "what is JavaScript": "JavaScript is a programming language that allows you to create interactive effects within web browsers.",
    "can you help with web development": "Of course! What do you need help with—HTML, CSS, JavaScript, or something else?",
    "what is SEO": "SEO (Search Engine Optimization) is the practice of optimizing your website to rank higher on search engines like Google.",
    "what is cloud computing": "Cloud computing is the delivery of computing services like servers, storage, and databases over the internet.",
    "what is a VPN": "A VPN (Virtual Private Network) provides a secure connection to the internet by encrypting your data and hiding your IP address.",
    "can you play a game": "I can't play games, but I can suggest some fun ones for you to try!",
    "what is quantum computing": "Quantum computing uses quantum mechanics principles to perform complex calculations at faster speeds than traditional computers.",
    "can you calculate": "Yes! Give me the problem, and I’ll calculate it for you.",
    "how do I calculate taxes": "Tax calculations depend on your location and tax bracket. You can use online calculators or consult an accountant for specifics.",
    "what is a blockchain": "Blockchain is a decentralized, digital ledger used to record transactions across many computers, ensuring security and transparency.",
    "what is cryptocurrency": "Cryptocurrency is a type of digital or virtual currency that uses cryptography for security, making it difficult to counterfeit or double-spend.",
    "how do I create a website": "Start by planning the layout, then use HTML for structure, CSS for styling, and JavaScript for interactivity.",
    "what is e-commerce": "E-commerce refers to buying and selling goods or services over the internet.",
    "how do I start a business": "Start by identifying a market need, creating a business plan, and securing funding or resources.",
    "what is digital marketing": "Digital marketing is the use of the internet, social media, and other online platforms to promote products and services.",
    "what is social media marketing": "Social media marketing involves using platforms like Facebook, Twitter, and Instagram to promote a brand and engage with customers.",
    "how do I make a presentation": "Start by outlining your key points, then use PowerPoint or Google Slides to create a visually appealing deck.",
    "what is a diet plan": "A diet plan is a structured approach to eating that helps you achieve specific health or fitness goals.",
    "how do I lose weight": "The best way to lose weight is through a combination of a balanced diet and regular exercise.",
    "can you give health tips": "Sure! Eat a balanced diet, exercise regularly, drink plenty of water, and get enough sleep.",
    "how do I stay motivated": "Set clear goals, track your progress, and reward yourself for milestones along the way."
}


# File paths
chat_history_file = "chat_history.json"        # File to store user input and chatbot responses
response_history_file = "responses_history.json"  # File to store only chatbot responses

# Function to load chat history from file
def load_chat_history():
    if os.path.exists(chat_history_file):
        with open(chat_history_file, 'r') as f:
            return json.load(f)
    else:
        return {"You": [], "Chatbot": []}  # Return an empty dictionary if file doesn't exist

# Function to load response history from file
def load_response_history():
    if os.path.exists(response_history_file):
        with open(response_history_file, 'r') as f:
            return json.load(f)
    else:
        return []  # Return an empty list if file doesn't exist

# Function to save chat history to file
def save_chat_history(chat_history):
    with open(chat_history_file, 'w') as f:
        json.dump(chat_history, f, indent=4)

# Function to save response history to file
def save_response_history(response_history):
    with open(response_history_file, 'w') as f:
        json.dump(response_history, f, indent=4)

# Function to get a response and update chat and response history
def get_response(user_input, chat_history):
    user_input = user_input.lower()  # Convert user input to lowercase to handle case insensitivity
    response = responses.get(user_input, responses["default"])

    # Add the user's message and the chatbot's response to the chat history
    chat_history["You"].append(user_input)
    chat_history["Chatbot"].append(response)

    # Load the previous response history
    response_history = load_response_history()
    # Add the new response to the response history
    response_history.append(response)

    # Save updated chat history and response history
    save_chat_history(chat_history)
    save_response_history(response_history)

    # Create a DataFrame from the chat history for visualization in a chart-like format
    chat_data = []
    for i in range(len(chat_history["You"])):
        chat_data.append([chat_history["You"][i], chat_history["Chatbot"][i]])

    # Return the DataFrame to be displayed as a chart and update chat history
    return chat_data, chat_history

# Gradio interface
def chatbot_interface():
    # Load chat history from the file at the start
    chat_history = load_chat_history()

    # Define the Gradio interface
    interface = gr.Interface(
        fn=get_response,  # Use the get_response function
        inputs=[gr.Textbox(label="Type your message", placeholder="Ask me something...", interactive=True),
                gr.State(chat_history)],  # Textbox for user input and state for chat history
        outputs=[gr.DataFrame(label="Chat History", interactive=False), gr.State()],  # Display chat history as DataFrame (chart-like)
        live=False,  # Disable live updates so response comes after pressing enter
        title="AI Chatbot",
        description="Chat with the AI chatbot and see the conversation history in a chart-like format.",
        theme="compact"
    )
    
    # Launch the interface
    interface.launch()

# Run the chatbot
if __name__ == "__main__":
    chatbot_interface()
