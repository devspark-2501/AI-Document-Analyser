from fastapi import FastAPI

# Initialize the FastAPI app instance
app = FastAPI(title="Document Analyser API", version="1.0.0")

@app.get("/health")
def health_check():
    """
    Health check endpoint to verify backend status and connectivity.
    """
    return {
        "status": "healthy",
        "message": "Document Analyser backend is up and running!"
    }