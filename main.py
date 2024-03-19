import configparser
import datetime
import postgres_mod as sql
import parser_mod as parser
import pathlib
from pathlib import Path

settings = configparser.ConfigParser()
settings.read('./parser4511/config.ini')
start_page = settings['links']['start_page']

clean_start = False
zero_launch = False
size_parser_launch = False
links_creation_launch = False
check_product_count = 100
main_parser_launch  = False

width_list = []
profile_list = []
diameter_list = []



if __name__ == "__main__":
    
    if clean_start: 
        sql.kill_all()
        
    if zero_launch: 
        sql.create_all()
        
    if size_parser_launch:
        width_list, profile_list, diameter_list = parser.take_size_grid(start_page)
        sql.flow_size_table(width_list, profile_list, diameter_list)
        
    if links_creation_launch: 
        sql.raw_flow_links_table()
        
    if check_product_count != 0:
        sum_links = sql.ask_links_sum()
        print(f'total in base: {sum_links} links')
        for i in range(1, check_product_count+1):
            current_link, current_sum = sql.take_link_from_table(link_id = i)
            wheels_counter = parser.how_many_products(current_link)
            print(f'\n{i} {datetime.datetime.now()} search in: {current_link}')
            print(f'found: {wheels_counter} wheels')