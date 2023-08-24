from scraper import Scraper

if __name__ == '__main__':
    primary_url = "https://www.state-machine.com/video-course"

    scpr = Scraper(primary_url)
    scpr.Fetch()
