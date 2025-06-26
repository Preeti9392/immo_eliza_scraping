from scraper_file import ImmowebScraper 
if __name__ == "__main__":
    scraper=ImmowebScraper(334)
    #scraper.get_urls_list()
    #scraper.immoweb_url_thread()
    scraper.thread_for_attrvalue()
    
    
    