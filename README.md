# GroundTruth Nexus: Hyper-Local GenAI Campaign Manager

### 🚀 Project Overview
Nexus is an AI-powered agent designed to democratize location-based advertising for small business owners. Leveraging GroundTruth's "Blueprints" technology and Generative AI (LLMs), Nexus automates the creation of hyper-local ad creatives based on real-time context (Weather, Events, Traffic).

### 🎯 The Problem
Small businesses (SMBs) struggle to utilize GroundTruth's powerful location targeting because they lack the resources to design dynamic, context-aware ad creatives.

### 💡 The Solution
A "Text-to-Campaign" agent where a user inputs a simple goal (e.g., "Sell more coffee on this rainy day"), and the AI:
1. **Analyzes Context:** Fetches real-time weather (OpenWeatherMap) and traffic data.
2. **Generates Creative:** Uses Gemini/GPT-4 to write punchy copy and generate relevant visuals.
3. **Optimizes Targeting:** Suggests a geofence radius based on the store's footfall history.

### 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **AI Core:** Google Gemini Pro / OpenAI GPT-4
* **Context API:** OpenWeatherMap API & Google Maps API
* **Integration:** Designed to integrate with GroundTruth's Ad Manager API

### 🚧 Current Status
* [x] Ideation & Architecture Design
* [x] Prototype: Weather-to-Ad-Copy Logic
* [ ] Integration with GroundTruth creative endpoint (In Progress)
