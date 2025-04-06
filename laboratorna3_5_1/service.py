from persistence import data_1, data_2
from domain import wind_dir


def ui_1(country, date_d):
    date_w = data_1(country, date_d) 
    if len(date_w) > 0:
        columns_name = ["country", "wind_degree", "wind_kph", "wind_direction", "last_updated", "sunrise", "sunset", "moonrise", "moonset", "goingoutside"]
        return columns_name
    else:
        return None
    
def ui_2(country, date_d):
    date_w = data_1(country, date_d)
    result = []
    if len(date_w) > 0:
        for i in date_w:
            data_h = data_2(i) 
            result.append((i.country, i.wind_degree, i.wind_kph, wind_dir(i.wind_direction).name, i.last_updated, data_h.sunrise, data_h.sunset, data_h.moonrise, data_h.moonset, data_h.goingoutside
            ))
        return result
    else:
        return None