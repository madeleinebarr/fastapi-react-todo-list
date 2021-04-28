import uvicorn

# define an entry point for running the application
# run a uvicorn server on port 8000 and reload on every file change
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
