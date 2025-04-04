from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Text, Integer, Float, Enum, DateTime, Time
import enum

class Base(DeclarativeBase):
    pass

class wind_dir(enum.Enum):
    NNW = "NNW"
    NW = "NW"
    W = "W"
    SW = "SW"
    SSE = "SSE"
    E = "E"
    N = "N"
    SE = "SE"
    ESE = "ESE"
    NNE = "NNE"
    S = "S"
    WSW = "WSW"
    SSW = "SSW"
    ENE = "ENE"
    NE = "NE"
    WNW = "WNW"


class world_weather(Base):
    __tablename__ = "WorldWeatherRepository"

    id: Mapped[int] = mapped_column(primary_key = True)
    country: Mapped[str] = mapped_column(Text)
    wind_degree: Mapped[int] = mapped_column(Integer)
    wind_kph: Mapped[float] = mapped_column(Float)
    wind_direction: Mapped[wind_dir] = mapped_column(Enum(wind_dir))
    last_updated: Mapped[DateTime] = mapped_column(DateTime)
    

class heavenly_bodies(Base):
    __tablename__ = "HeavenlyBodies"

    id: Mapped[int] = mapped_column(primary_key=True)
    sunrise: Mapped[Time] = mapped_column(Time)
    sunset: Mapped[Time] = mapped_column(Time)
    moonrise: Mapped[Time] = mapped_column(Time, nullable = True)
    moonset: Mapped[Time] = mapped_column(Time, nullable = True)