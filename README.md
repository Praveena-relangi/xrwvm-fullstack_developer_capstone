# Car Dealership Website - Final Project  

This repository contains the final project for the Full Stack Web Development course, showcasing a fully functional car dealership website built with Django, React, Node.js, MongoDB, and other modern technologies. The project demonstrates an end-to-end application with backend, frontend, and cloud deployment components.

## Architecture Overview  

The project is divided into multiple steps to guide the development process, focusing on implementing features in smaller modules. Below is a high-level overview of the architecture and workflow:  

1. **Frontend:** React for dynamic user interactions.  
2. **Backend:** Django and Node.js for business logic and microservices.  
3. **Database:** SQLite for Django models; MongoDB for dealership and review management.  
4. **Sentiment Analysis:** IBM Cloud Code Engine for real-time sentiment analysis of reviews.  
5. **Deployment:** Kubernetes and Docker for hosting and scaling services.  

## Project Breakdown  

### Steps:  
1. **Repository Setup:**  
   - Forked and cloned the provided GitHub template.  
   - Worked on static and dynamic pages.  

2. **User Management:**  
   - Added Django's user authentication system.  
   - Integrated React for the frontend user experience.  

3. **Backend Services:**  
   - Developed a Node.js microservice for dealer and review management using MongoDB.  
   - Dockerized the Node.js application for easy deployment.  

4. **Django Features:**  
   - Created models and views for `Car Make` and `Car Model`.  
   - Implemented proxy services to integrate dealer and review microservices.  
   - Developed dynamic pages for displaying dealers, reviews, and adding new reviews.  

5. **Sentiment Analysis:**  
   - Deployed a sentiment analyzer service on IBM Cloud Code Engine.  
   - Integrated the service with the Django application for analyzing review sentiments.  

6. **CI/CD Pipeline:**  
   - Set up continuous integration for code linting and automated testing.  
   - Deployed the application on Kubernetes for scalability.  

## Solution Architecture  

The solution is a multi-service application with the following components:  

1. **Django Application (Dealership Website):**  
   - Provides web pages for user interaction.  
   - Includes APIs for fetching cars, dealers, and managing reviews.  

2. **Node.js Service (Dealership and Reviews):**  
   - Manages dealership and review data using MongoDB.  
   - Exposed APIs include `/fetchDealers`, `/fetchReviews`, and `/insertReview`.  

3. **Sentiment Analyzer Service:**  
   - Analyzes review sentiments (`positive`, `neutral`, or `negative`) using a REST API.  

4. **Databases:**  
   - SQLite for storing car make and model data.  
   - MongoDB for dealerships and reviews.  

5. **Integration:**  
   - Django Proxy Service acts as a bridge between the web app and external microservices.  

### Key Endpoints  

#### Django Application:  
- `/get_cars/` - Fetch list of cars.  
- `/get_dealers/` - Fetch list of dealers.  
- `/get_dealers/:state` - Fetch dealers by state.  
- `/dealer/:id` - Fetch dealer details by ID.  
- `/review/dealer/:id` - Fetch reviews for a dealer.  
- `/add_review/` - Add a review.  

#### Node.js Service:  
- `/fetchDealers` - Fetch all dealers.  
- `/fetchDealer/:id` - Fetch dealer details by ID.  
- `/fetchReviews` - Fetch all reviews.  
- `/fetchReview/dealer/:id` - Fetch reviews for a specific dealer.  
- `/insertReview` - Add a new review.  

#### Sentiment Analyzer:  
- `/analyze/:text` - Analyze review sentiment.  

## Deployment  

- **Local Development:**  
  - Application tested locally using Cloud IDE.  

- **Docker:**  
  - Node.js services dockerized for streamlined deployment.  

- **Kubernetes:**  
  - Deployed the application on Kubernetes for scalability.  

- **CI/CD:**  
  - Continuous integration pipeline implemented for efficient delivery and quality assurance.  

## Screenshots  

Please refer to the `screenshots` folder for images documenting the project stages and features.  

## How to Run  

1. Clone this repository:  
   ```bash
   git clone <repo-url>
   cd <project-folder>
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   npm install
   ```  
3. Run services:  
   ```bash
   python manage.py runserver
   node server.js
   ```  
4. Open the application in a browser at `http://localhost:8000`.  

---
