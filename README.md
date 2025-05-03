# SysML Activity Diagram Analyzer

A web application for analyzing SysML Activity Diagrams to identify system safety aspects relevant to aerospace engineering.

## Project Structure

```
ai-mbse/
├── frontend/          # React + TypeScript frontend
├── backend/           # FastAPI Python backend
```

## Local Development

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the backend server:
```bash
cd app
uvicorn main:app --reload
```

The backend will be available at http://localhost:8000

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at http://localhost:5173

## Deployment

### Backend Deployment (Render)

1. Create a new Web Service on [Render](https://render.com)
2. Connect your GitHub repository
3. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `cd app && uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Add environment variables in Render dashboard

### Frontend Deployment (Vercel)

1. Create a new project on [Vercel](https://vercel.com)
2. Connect your GitHub repository
3. Configure the following:
   - Framework Preset: Vite
   - Root Directory: frontend
   - Build Command: `npm run build`
   - Output Directory: dist
4. Add environment variables in Vercel dashboard:
   - VITE_API_URL: Your local API URL (for development)
   - VITE_PROD_API_URL: Your production API URL from Render

## License

MIT License - see [LICENSE](LICENSE) for details 