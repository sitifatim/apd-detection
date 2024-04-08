from db.database import *
from db.model import *

from sqlalchemy import select, text
from sqlalchemy.sql import func 
from datetime import datetime
from sqlalchemy.orm import aliased
from sqlalchemy.orm import query

import json
from datetime import date, timedelta, timezone, datetime


from PIL import Image
import base64
from io import BytesIO
import numpy as np

def convert_image(image_data):
    image = Image.open(BytesIO(image_data))
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

def convert_time_delta(duration):
    if duration is not None:
        total_seconds = duration.total_seconds()
        hours = total_seconds/3600
        remaining_seconds = total_seconds%3600
        minutes = remaining_seconds//60
        seconds = remaining_seconds%60
        return total_seconds
    else:
        return None
    
def convert_time_duration(duration):
    if duration is not None:
        total_seconds = duration
        hours = total_seconds//3600
        remaining_seconds = total_seconds%3600
        minutes = remaining_seconds//60
        seconds = remaining_seconds%60
        return f'{int(hours)}H {int(minutes)}M'
    else:
        return ''
    
def convert_time(data):
    try:
        return data.strftime("%H:%M:%S")
    except AttributeError:
        return ''

def convert_time_day(daydate):
    date_object = daydate.strftime("%d/%m/%Y")
    # days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday"]
    # day_of_week_index = int(date_object.strftime('%w'))
    # day_of_week = days_of_week[day_of_week_index]
    # local_time = date_object.strftime('%A, %d %B %Y')
    return date_object

def insert_image_detect(image, created_at):
    session = Session()
    query = DaftarFR(image_captured= image, created_at=created_at)
    session.add(query)
    session.commit()
    session.close()

def get_detect_today():
    session = Session()
    count = session.query(func.count()).filter(DaftarFR.created_at == func.current_date()).scalar()
    session.close()
    return count

def get_data_detect():
    # data_lists = []
    session=Session()
    query = select(DaftarFR.image_captured, DaftarFR.created_at).where(DaftarFR.created_at == func.current_date())
    url = session.execute(query).fetchall()
    session.close()

    data_lists = [[convert_image(item[0]), item[1].strftime('%H:%M:%S')] for item in url]
    
    # data_lists.append([recognize, score, image, date_time, greeting_audio])
    
    return data_lists

def get_image_detect():
    # data_lists = []
    session=Session()
    query = select(DaftarFR.image_captured, DaftarFR.created_at)
    url = session.execute(query).fetchall()
    session.close()

    data_lists = [[convert_image(item[0]), item[1].strftime('%H:%M:%S')] for item in url]
    
    # data_lists.append([recognize, score, image, date_time, greeting_audio])
    
    return data_lists

