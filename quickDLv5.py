import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import filedialog
import os

root = tk.Tk()
root.title("File Downloader")
root.geometry("600x400")

url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

file_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

file_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=file_listbox.yview)

def get_links():
    url = url_entry.get()
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for link in soup.find_all('a'):
        href = link.get('href')
        if href.endswith(('.jpg', '.jpeg', '.png', '.gif', '.mp4', '.pdf', '.doc', '.docx', '.txt')):
            add_file_to_listbox(url + href)

def add_file_to_listbox(file_url):
    filename = file_url.split('/')[-1]
    file_extension = filename.split('.')[-1]
    file_size = get_file_size(file_url)
    file_listbox.insert(tk.END, "{} - {} - {} bytes".format(filename, file_extension, file_size))

def get_file_size(file_url):
    r = requests.head(file_url)
    if 'Content-Length' in r.headers:
        return int(r.headers['Content-Length'])
    else:
        return 0

def download_files():
    url = url_entry.get()
    files = file_listbox.curselection()

    # ask the user to select the download directory
    download_dir = filedialog.askdirectory()
    if not download_dir:
        return  # user cancelled, do nothing

    for file in files:
        filename = file_listbox.get(file).split(' - ')[0]
        r = requests.get(url + filename, stream=True)
        with open(os.path.join(download_dir, filename), 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            dl = 0
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    dl += len(chunk)
                    f.write(chunk)
                    f.flush()
                    progress = dl / total_length * 100
                    progress_label.config(text="Downloading {} - {:.2f}%".format(filename, progress))

    progress_label.config(text="Download complete!")


progress_label = tk.Label(root, text="")
progress_label.pack()


get_links_button = tk.Button(root, text="Get Links", command=get_links)
get_links_button.pack()

download_button = tk.Button(root, text="Download", command=download_files)
download_button.pack()

root.mainloop()
