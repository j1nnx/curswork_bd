import requests


class HHApi:
    BASE_URL = "https://api.hh.ru"

    @staticmethod
    def get_employer_data(employer_id):
        """Fetches detailed information about an employer by their ID."""
        url = f'{HHApi.BASE_URL}/employers/{employer_id}'  # connect in hh.api in table employers
        response = requests.get(url)
        response.raise_for_status()  # Ensures HTTP errors are caught and raised.
        return response.json()

    @staticmethod
    def get_vacancies(employer_id):
        """Fetches all vacancies associated with a given employer ID."""
        url = f'{HHApi.BASE_URL}/vacancies'  # connect in hh.api in table vacancies
        params = {"employer_id": employer_id, "per_page": 100}  # Limits results to 100 per page.
        response = requests.get(url, params=params)
        response.raise_for_status()  # Ensures the request was successful.
        return response.json().get('items', [])  # Returns a list of vacancies.
