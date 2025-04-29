from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re
import json
import time

# Function to fetch the webpage content using Selenium
def fetch_webpage_with_selenium(driver, url):
    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to load completely
        return driver.page_source
    except Exception as e:
        print(f"Error fetching URL {url}: {e}")
        return None

# Function to parse the HTML content and extract news articles
def parse_articles(driver, html_content, limit):
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = []

    # Check if the news-list section exists
    news_list_section = soup.select_one('.news-list')
    if not news_list_section:
        return articles

    # Select links inside the 'news-list' section with class 'news-list__item'
    news_items = news_list_section.select('.news-list__item a')

    # Process only up to the specified limit
    for item in news_items[:limit]:
        link = item['href']
        if re.match(r'^/news/easy/ne\d+/ne\d+\.html$', link):  # Match "ne*" pattern
            full_link = f"https://www3.nhk.or.jp{link}"  # Construct full URL
            time.sleep(2.5)  # Add a 2.5-second delay before fetching the article page
            article_html = fetch_webpage_with_selenium(driver, full_link)  # Fetch the article page
            if not article_html:
                continue
            article_soup = BeautifulSoup(article_html, 'html.parser')

            # Extract required elements
            title = article_soup.select_one('.article-title')
            date = article_soup.select_one('.article-date')
            body = article_soup.select_one('.article-body')

            if title and date and body:
                articles.append({
                    'title': title.get_text(strip=True),
                    'date': date.get_text(strip=True),
                    'body': body.get_text(strip=True),
                    'link': full_link
                })

            # Stop if the desired number of articles is reached
            if len(articles) >= limit:
                break

    return articles

# Main function to run the scraper
def main():
    url = 'https://www3.nhk.or.jp/news/easy/'
    service = Service('/usr/local/bin/chromedriver')  # Use the ChromeDriver path for GitHub Actions
    driver = webdriver.Chrome(service=service)

    try:
        # Set the number of articles to scrape to 10
        scrape_count = 10

        # Fetch the main page content
        html_content = fetch_webpage_with_selenium(driver, url)
        if not html_content:
            print("Failed to fetch the main page content.")
            return

        # Parse and fetch the specified number of articles
        articles = parse_articles(driver, html_content, scrape_count)

        # Write the result to output.json
        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(articles, f, ensure_ascii=False, indent=4)

        print("Scraping completed. Results saved to output.json.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()  # Ensure the browser is closed properly

if __name__ == "__main__":
    main()