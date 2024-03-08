import logging
from fastapi import FastAPI, BackgroundTasks, Request
from fastapi.responses import JSONResponse
from app.etl.extract import extract_data
from app.etl.transform import transform_data
from app.etl.load import load_data
from app.api.routes import router  

app = FastAPI()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status code: {response.status_code}")
    return response

@app.get("/")
async def root():
    logger.info("Processing root endpoint")
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    logger.info(f"Processing read_item endpoint with item_id: {item_id}")
    return {"item_id": item_id}

@app.post("/etl")
async def run_etl(background_tasks: BackgroundTasks):
    logger.info("Triggering ETL workflow")
    background_tasks.add_task(etl_workflow)
    return {"message": "ETL workflow started"}

async def etl_workflow():
    try:
        logger.info("Starting ETL workflow")

        
        logger.info("Extracting data from the source")
        extracted_data = extract_data()

        # Transform the extracted data
        logger.info("Transforming the extracted data")
        transformed_data = transform_data(extracted_data)

        
        logger.info("Loading the transformed data into the destination")
        load_data(transformed_data)

        logger.info("ETL workflow completed successfully")
    except Exception as exc:
        logger.error(f"An error occurred during the ETL workflow: {str(exc)}")

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.error(f"An error occurred: {str(exc)}")
    return JSONResponse(content={"error": "Internal Server Error"}, status_code=500)

app.include_router(router)  