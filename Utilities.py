from bs4 import BeautifulSoup
import requests

class Validity_Checker: 
    
    def checkCity (self, city: str):
        url = "https://www.britannica.com/topic/list-of-cities-and-towns-in-Canada-2038873"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        match = False
        
        for item in soup.select ('.md-crosslink'):
            if city.lower() == item.get_text().lower():
                match = True
        
        return match
    
    
        
        