# SysML Activity Diagram Analyzer

A web application that analyzes SysML Activity Diagrams using OpenAI's GPT-4 Vision model, focusing on system safety aspects relevant to aerospace engineering.

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- OpenAI API key

## Getting an OpenAI API Key

1. Go to [OpenAI's website](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to the API keys section
4. Create a new API key
5. Copy the API key to use in the application

## Setting Up the Environment

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Running the Application

1. Start the backend server:
   ```bash
   cd backend
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   uvicorn app.main:app --reload
   ```

2. In a new terminal, start the frontend development server:
   ```bash
   cd frontend
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:5173`

## Usage

1. Click on the "Upload a file" button or drag and drop a SysML Activity Diagram image
2. Click "Analyze Diagram" to process the image
3. View the analysis results below the image

## Features

- User-friendly interface for uploading SysML Activity Diagrams
- Real-time image preview
- Analysis of system safety aspects using OpenAI's GPT-4 Vision model
- Error handling and loading states
- Responsive design

## Security Notes

- The OpenAI API key is stored in the `.env` file and should never be committed to version control
- In production, implement proper CORS policies and API key management
- Consider implementing rate limiting and other security measures

## License

MIT 