# googlescraper-cli
Scrape Google SERP from command line.

## Instructions
* Download or Clone the repository.
```commandline
git clone git://github.com/SU-SWS/open_framework.git
```
* Install the requirements.
```commandline
pip install -r requirements.txt
```
* Run the cli
```commandline
python googlescraper-cli.py --query "baseball" --limit 20
```
* Output will be stored in a CSV file `google_scrape_results-[query].csv`

## Arguments
### Query
`-q` or `--query`

The search query to be scraped. Required argument.

### Limit
`-l` or `--limit`

Number of results to be scraped. Default value is 10.

## Dependencies
* Selenium