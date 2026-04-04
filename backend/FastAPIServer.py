from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI(title="SyllabiXtract API")

# Configure CORS (Cross-Origin Resource Sharing)
# This allows the React frontend (on localhost or Vercel) to talk to this backend
# Tell the backend to accept requests from the internet
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "SyllabiXtract Backend is running!"}

@app.post("/upload")
async def handle_syllabus_upload(file: UploadFile = File(...)):
    """
    This is the endpoint that receives the PDF from React.
    Later, add the LlamaParse and Gemini logic here.
    """
    # For now, just prove that we received the file successfully
    file_size = len(await file.read())
    
    print(f"Received file: {file.filename} ({file_size} bytes)")
    
    # Send a mock response back to React
    return {
        "status": "success",
        "filename": file.filename,
        "message": "File received by FastAPI. AI extraction coming soon!",
        "mock_events": [
            {"title": "Midterm Exam", "date": "2026-10-15"},
            {"title": "Final Project Due", "date": "2026-12-10"}
        ]
    }