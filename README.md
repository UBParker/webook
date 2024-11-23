# we.book

**we.book** is an open-source project aimed at creating the first agentic AI capable of booking flights seamlessly. Built using cutting-edge open-source technologies, this project combines natural language understanding (NLU), API integration, and task automation to revolutionize how users plan and book their travel.

This repository is licensed under the MIT License for non-commercial use. For commercial use, please contact ash.marie.parker@gmail.com for licensing terms.

---

## 🌟 Features
- **Natural Language Understanding (NLU):** Understand user queries such as "Find me a flight to Paris on December 15th."
- **Flight Search Integration:** Connect with popular flight search APIs like Amadeus, Skyscanner, and Kiwi.
- **Personalized Recommendations:** Offer flight options tailored to user preferences (e.g., price, duration, layovers).
- **Secure Booking Workflow:** Finalize bookings directly through airline or travel service APIs.
- **Expandable Architecture:** Future support for adjacent services like hotel reservations and car rentals.

---

## 🛠️ Tech Stack
- **Language:** Python
- **Backend Framework:** FastAPI
- **NLU Framework:** Rasa / spaCy with Transformers
- **Task Automation:** Celery with Redis
- **Database:** PostgreSQL (or SQLite for development)
- **Frontend (Planned):** CLI (initial MVP), optional web interface with Streamlit or React.js
- **APIs:** Amadeus for Developers, Skyscanner API, Kiwi API

---

## 🚀 Project Roadmap
### Phase 1: Core Functionality
1. Set up the backend using FastAPI.
2. Train the NLU model to handle flight-related queries.
3. Integrate flight search APIs for real-time results.

### Phase 2: Advanced Features
1. Implement a recommendation system for ranking flight options.
2. Add secure booking workflows using API integrations.
3. Store user preferences and booking history in the database.

### Phase 3: User Experience
1. Develop a simple CLI for MVP testing.
2. Expand to a web-based frontend for broader accessibility.
3. Perform testing and deploy the platform.

---

## 📖 How to Get Started
### Prerequisites
- Python 3.9 or later
- PostgreSQL or SQLite (for database)
- Redis (for task automation)

### Installation
1. Clone the repository:
   ```
   bash
   git clone https://github.com/UBParker/webook.git
   cd webook
   ```
2. Install dependencies:
   ```
   pip install rasa
   pip install -r requirements.txt
   
   ```
   
3. Set up environment variables:
- Create a .env file in the root directory.
- Add the following variables to the .env file:
    ```
    API_KEY=your_flight_api_key
    DATABASE_URL=postgresql://user:password@localhost:5432/webook
    REDIS_URL=redis://localhost:6379/0

    ```
4. Run the backend server:   
   ```
   uvicorn main:app --reload
   ```

   
