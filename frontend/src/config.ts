const config = {
  apiUrl: import.meta.env.PROD 
    ? 'https://ai-mbse.onrender.com'
    : 'http://localhost:8000'
}

export default config; 