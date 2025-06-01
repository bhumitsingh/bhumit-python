import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_pdfs_from_website(url, download_folder="pdfs"):
    # Create folder if not exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    pdf_links = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.lower().endswith(".pdf"):
            full_url = urljoin(url, href)
            pdf_links.append(full_url)

    if not pdf_links:
        print("No PDF files found.")
        return

    print(f"Found {len(pdf_links)} PDF(s). Downloading...")

    for i, pdf_url in enumerate(pdf_links, 1):
        try:
            pdf_response = requests.get(pdf_url)
            pdf_response.raise_for_status()

            filename = os.path.join(download_folder, os.path.basename(urlparse(pdf_url).path))
            with open(filename, 'wb') as f:
                f.write(pdf_response.content)
            print(f"[{i}] Downloaded: {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {pdf_url}: {e}")

# Example usage:
website_url = "https://www.icai.org/post/19141"  # Replace with the target website URL
download_pdfs_from_website(website_url)
