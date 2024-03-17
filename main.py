import configparser
import postgres_mod as sql
import parser_mod as parser
import pathlib
from pathlib import Path

settings = configparser.ConfigParser()
settings.read('./parser4511/config.ini')
start_page = settings['links']['start_page']

clean_start = False
zero_launch = True
size_parser_launch = False
links_creation_launch = True
check_product_count = False
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
        
    if check_product_count: 
        sql.check_links()