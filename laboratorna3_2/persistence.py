from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain import Base, world_weather, wind_dir
from datetime import datetime
import pandas as pd

def read_dt():
    df_read = pd.read_csv("GlobalWeatherRepository.csv", delimiter = ",")
    return df_read

engine = create_engine("postgresql+psycopg2://postgres:4712@localhost:5432/laboratorna3")

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

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