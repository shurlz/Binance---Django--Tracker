from .models import coinStore
from .scraper import binance_scraper
from celery import shared_task


@shared_task
def save_to_database():
    scrapped_data = binance_scraper()
    
    coins_num = range(len(scrapped_data))
    for count in coins_num:
        new_instance = coinStore(name=scrapped_data["names"][count], symbol=scrapped_data["symbols"][count], 
                        price=scrapped_data["prices"][count], change=scrapped_data["changes"][count], 
                        volume=scrapped_data["volumes"][count], market_cap=scrapped_data["market_caps"][count])
        new_instance.save()
    
    return True

