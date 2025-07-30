# AI Trip Planner 🌍✈️

[![LLMOps](https://img.shields.io/badge/LLMOps-Enabled-green.svg)](https://github.com/atharvahatekar/AI-TRIP-PLANNER)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-orange.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-blue.svg)](https://python.langchain.com/)
[![Docker](https://img.shields.io/badge/Docker-Compatible-blue.svg)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-blue.svg)](https://kubernetes.io/)

An AI-powered travel itinerary planner that creates personalized trip recommendations based on your destination, interests, and preferences. This application leverages Large Language Models and follows LLMOps practices to deliver high-quality, customized travel plans.

![AI Trip Planner Screenshot](https://via.placeholder.com/800x400?text=AI+Trip+Planner+Screenshot)

## ✨ Features

- **Personalized Travel Itineraries**: Generate detailed day-by-day travel plans based on your preferences
- **Multiple Parameters**:
  - Destination city selection
  - Interest-based recommendations
  - Customizable trip duration
  - Budget level preferences
  - Travel style options (Family-friendly, Adventure, Cultural, etc.)
  - Seasonal recommendations
  - Accessibility considerations
- **Dark Theme UI**: Modern, sleek dark-themed interface
- **Rich Information**:
  - Structured day-by-day plans
  - Morning, afternoon, and evening activities
  - Restaurant recommendations
  - Budget-appropriate suggestions
  - Local tips and cultural insights
- **Save & Export**: Download your itineraries in JSON or text formats
- **Mobile-Responsive**: Works on desktop and mobile devices

## 🛠️ Tech Stack

This project implements a modular architecture and LLMOps (Large Language Model Operations) practices, using:

### Core Technologies
- **Python 3.10**: Base programming language
- **Streamlit**: Frontend web application framework
- **LangChain**: Framework for LLM application development
  - LangChain Core
  - LangChain Groq
  - LangChain Community
- **LLaMA 3.3 70B**: Large Language Model for generating itineraries
- **Groq API**: High-speed LLM inference
- **Python-dotenv**: Environment variable management

### LLMOps & Infrastructure
- **Docker**: Containerization for consistent deployment
- **Kubernetes**: Container orchestration for scaling
- **ELK Stack**: Logging and monitoring
  - Elasticsearch: Log storage and search
  - Logstash: Log processing pipeline
  - Kibana: Log visualization
  - Filebeat: Log shipping
- **Modular Python Architecture**: Clean separation of concerns


## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Groq API key (for LLM access)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/atharvahatekar/AI-TRIP-PLANNER.git
   cd AI-TRIP-PLANNER
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -e .
   ```

4. Create a `.env` file with your API keys
   ```
   GROQ_API_KEY=your_groq_api_key
   ```

5. Run the application
   ```bash
   streamlit run app.py
   ```

### Using Docker

1. Build the Docker image
   ```bash
   docker build -t ai-trip-planner:latest .
   ```

2. Run the Docker container
   ```bash
   docker run -p 8501:8501 -e GROQ_API_KEY=your_groq_api_key ai-trip-planner:latest
   ```

### Kubernetes Deployment

1. Create a secret for your API keys
   ```bash
   kubectl create namespace logging
   kubectl create secret generic llmops-secrets --from-literal=GROQ_API_KEY=your_groq_api_key
   ```

2. Deploy the application and ELK stack
   ```bash
   kubectl apply -f elasticsearch.yaml
   kubectl apply -f logstash.yaml
   kubectl apply -f kibana.yaml
   kubectl apply -f filebeat.yaml
   kubectl apply -f k8s-deployment.yaml
   ```

## 📊 LLMOps Implementation

This project follows LLMOps best practices:

1. **Modular Architecture**: Clean separation between UI, business logic, and LLM integration
2. **Robust Logging**: Comprehensive logging system for monitoring and debugging
3. **Containerization**: Docker for consistent environments across development and production
4. **Orchestration**: Kubernetes for scaling and management
5. **Monitoring**: ELK stack for log aggregation and analysis
6. **CI/CD Ready**: Structure prepared for continuous integration and deployment
7. **Exception Handling**: Custom exceptions for better error management

## 📝 Project Workflow

1. User enters their travel preferences (destination, interests, duration, budget, etc.)
2. The application processes these inputs through the TravelPlanner class
3. LangChain constructs an optimized prompt for the LLaMA 3.3 70B model via Groq
4. The LLM generates a detailed, personalized travel itinerary
5. Results are presented in an intuitive, visually appealing interface
6. User can save or export their itinerary for future reference

## 🛡️ Future Enhancements

- Integration with real-time travel APIs for up-to-date information
- User accounts for saving and managing multiple itineraries
- Social sharing capabilities
- Interactive map integration with points of interest
- Multi-language support
- Mobile application version

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Atharva Hatekar**

---

*Created with LLMOps practices and modular Python architecture*
