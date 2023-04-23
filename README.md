# file-grabber
The given code is a Python script that creates a graphical user interface (GUI) for a file downloader application using the Tkinter library. When executed, the GUI window will appear with an entry box for the user to enter a URL, a "Get Links" button to extract links from the URL, a listbox to display the links, a scrollbar to scroll through the links, and a "Download" button to download the selected files from the listbox. The application can download files with extensions such as .jpg, .jpeg, .png, .gif, .mp4, .pdf, .doc, .docx, and .txt.

The code begins by importing necessary modules such as Tkinter, requests, BeautifulSoup, and os. It then creates a root Tkinter object, sets the title and size of the GUI window. Next, it creates a label and an entry box to enter a URL, followed by a listbox to display the files available for download. A scrollbar is created and attached to the listbox for scrolling through the files.

The code defines three functions: "get_links()", "add_file_to_listbox()", and "download_files()".

The "get_links()" function takes the URL entered in the entry box and sends an HTTP GET request to the URL using the requests library. It then parses the content of the page using the BeautifulSoup library and extracts all links with file extensions matching the ones specified in the code. It then calls the "add_file_to_listbox()" function to add the file information to the listbox.

The "add_file_to_listbox()" function takes a file URL, extracts the filename, file extension, and file size and formats it as a string to display in the listbox.

The "download_files()" function is called when the "Download" button is clicked. It retrieves the URL entered in the entry box and the selected files in the listbox. It prompts the user to select a download directory using the filedialog module. For each selected file, it sends an HTTP GET request to the URL and downloads the file to the selected directory using the requests and os libraries. It updates a progress label in the GUI with the current download progress.

Finally, the script creates "Get Links" and "Download" buttons and a progress label, and associates them with the functions defined above. It starts the Tkinter main loop to display the GUI window and wait for user interactions.
