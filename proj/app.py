from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
from core.pipeline.Prediction_pipeline import CustomData, PredictPipeline

app = FastAPI()

# Static files for CSS and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "results": None})

@app.post("/", response_class=HTMLResponse)
async def predict_datapoint(
    request: Request,
    gender: str = Form(...),
    ethnicity: str = Form(...),
    parental_level_of_education: str = Form(...),
    lunch: str = Form(...),
    test_preparation_course: str = Form(...),
    reading_score: float = Form(...),
    writing_score: float = Form(...)
):
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )
    pred_df = data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    return templates.TemplateResponse("home.html", {"request": request, "results": results[0]})
