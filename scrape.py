import threading
import urllib.request

# Define a function for each thread to download a URL
def download_url(url):
    filename = url.split("/")[-1]  # Extract the filename from the URL
    urllib.request.urlretrieve(url, filename)  # Download the file

# Open the URLs file and read each URL into a list
with open("urls.txt", "r") as f:
    urls = [line.strip() for line in f.readlines()]

# Create a thread for each URL and start them all simultaneously
threads = []
for url in urls:
    thread = threading.Thread(target=download_url, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All files downloaded successfully.")
