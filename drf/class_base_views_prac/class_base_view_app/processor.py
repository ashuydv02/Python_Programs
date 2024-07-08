import datetime

def get_current_datetime(request):
    current_date_time = datetime.datetime.now()
    return {'current_date_time': current_date_time}
