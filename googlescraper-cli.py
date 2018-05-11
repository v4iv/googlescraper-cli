import argparse, time
from scraper import scrape_google, init_driver


def get_parser():
    """Get parser for command line arguments."""
    arg_parser = argparse.ArgumentParser(description="Python Based Web Stats Generator")
    arg_parser.add_argument("-q",
                            "--query",
                            dest="query",
                            help="Query To Be Scrapped from Google")
    arg_parser.add_argument("-l",
                            "--limit",
                            dest="limit",
                            help="Number of Search Results To Be Scraped")
    return arg_parser


arguments = get_parser()
args = arguments.parse_args()
QUERY = args.query
LIMIT = args.limit

if __name__ == "__main__":
    driver = init_driver()
    scrape_google(driver, QUERY, LIMIT)
    time.sleep(5)
    driver.quit()
