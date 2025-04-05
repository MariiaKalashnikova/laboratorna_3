from sqlalchemy import create_engine, Date, cast
from sqlalchemy.orm import sessionmaker
from domain import Base, world_weather, wind_dir, heavenly_bodies
from datetime import datetime
import pandas as pd
#from service import fill_column

def read_dt():
    df_read = pd.read_csv("GlobalWeatherRepository.csv", delimiter = ",")
    return df_read

engine = create_engine("postgresql+psycopg2://postgres:4712@localhost:5432/laboratorna3")

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

if session.query(world_weather).count() == 0:
    df = read_dt()

    for i in df.itertuples(index = False):
        session.add(world_weather(
            country = i.country,
            wind_degree = i.wind_degree,
            wind_kph = i.wind_kph,
            wind_direction = wind_dir[i.wind_direction],
            last_updated = datetime.strptime(i.last_updated, "%Y-%m-%d %H:%M"),
        
            sunrise = datetime.strptime(i.sunrise, "%I:%M %p"),
            sunset = datetime.strptime(i.sunset, "%I:%M %p"),
            moonrise = datetime.strptime(i.moonrise, "%I:%M %p") if(i.moonrise != "No moonrise") else None,
            moonset = datetime.strptime(i.moonset, "%I:%M %p") if(i.moonset != "No moonset") else None
        ))

    session.commit()
session.close()

engine = create_engine("postgresql+psycopg2://postgres:4712@localhost:5432/laboratorna3")
Session1 = sessionmaker(bind=engine)
session1 = Session1()


data = session1.query(world_weather.id, world_weather.wind_direction).all()

for weather in data:  
    from service import fill_column
    heavenly_body = session1.query(heavenly_bodies).filter(heavenly_bodies.id == weather.id).first()    
    if heavenly_body:   
        heavenly_body.goingoutside = fill_column(weather.wind_direction, wind_dir.N, wind_dir.S)
        

session1.commit()
session1.close()

engine = create_engine("postgresql+psycopg2://postgres:4712@localhost:5432/laboratorna3")
Session2 = sessionmaker(bind=engine)
session2 = Session2()


def data_1(country, date_d):
    date_w = session2.query(world_weather).filter((world_weather.country == country) & (cast(world_weather.last_updated, Date) == date_d)).all()
    return date_w

def data_2(i):
    data_h = session2.query(heavenly_bodies).filter(heavenly_bodies.id == i.id).first()
    return data_h

