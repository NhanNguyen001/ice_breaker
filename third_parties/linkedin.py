from http.client import responses

import requests
import os
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from linkedin profiles,
    Manually scrape the information from the Linkedin profile"""
    print(linkedin_profile_url)

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/NhanNguyen001/9d6863c7706c1f4187278e895f04bd97/raw/20fdd0faca6ec7d858fddcabd0f31915333316bf/eden-marco.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        api_key = os.environ["PROXYCURL_API_KEY"]
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            'linkedin_profile_url': linkedin_profile_url
        }
        response = requests.get(
            api_endpoint,
            params=params,
            headers=headers,
            timeout=10
        )

    data = response.json()

    data = {
        k: v
        for k,v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certification"]
    }
    if data.get("groups"):
        for group in data.get("groups"):
            group.pop("profile_pic_url")

    return data

if __name__ == '__main__':
    print(
        scrape_linkedin(
            linkedin_profile_url=os.getenv('https://www.linkedin.com/in/nhannguyen2895/'),
            mock=False
        )
    )