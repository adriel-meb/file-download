import requests
import re
import os

"""
Simple python script to download any file on the internet
and save it in the current directory
"""

def check_url(url_link):
    """Check if URL is valid """
    res = requests.get(url_link, allow_redirects =True)
    if res.status_code == 200:
        print('valid URL \n')
        return url_link
    else:
        print('Oupps there is something wrong with your URL. Run the program again!! ')
        return res.status_code
        
def extract_file_extension(url_file):
    """Extract the extension from url"""
    pattern = re.split("\.",url_file)
    return pattern[-1]


def download_and_save(url, file_name,file_extension):
    """ download and save the file to the working directory"""
    #make a request for the file
    response = requests.get(url, allow_redirects =True)

    #compose the file + extension
    file_to_be_saved = f"{file_name}.{file_extension}"
    
    #Create a new file with "file_to_be_saved" in the current directory
    # And save this file and print the directory with the OS module
    with open(file_to_be_saved, 'wb') as file:
        print("saving file.... \n")
        file.write(response.content)
        print('done....\n')
        print('file saved as:  ', file_to_be_saved )
        print('in:  ', os.getcwd() )
    
    

def main():
    #User enter the URL of the file to be downloaded
    url_to_check = input('Enter the url of the file to download : \n')
    
    #check if the URL is valid, if not the program ends
    url = check_url(url_to_check)
    
    #extract the extension of the file (.jpg, .pdf, .csv, etc...)
    file_extension = extract_file_extension(url)
    
    #User enter how he/she ants the downloaded file to be named
    file_name= input('Enter how you want the file to be named(do not write the extension) : ')

    #download and save the file to the current directory
    download_and_save(url, file_name,file_extension)

    
    

if __name__ == "__main__":
    main()