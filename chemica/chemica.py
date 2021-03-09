from dataclasses import dataclass
from typing import List, Union
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@dataclass
class Equation:
    """The object represents a chemical reaction."""
    substances: tuple
    result: str


@dataclass
class Substance:
    """This object represents a chemical substance."""
    substance: str
    name: str
    condition: str


class _Request(urllib3.HTTPConnectionPool):
    @staticmethod
    def make(method: str, url: str) -> urllib3.HTTPResponse:
        return urllib3.PoolManager(cert_reqs="CERT_NONE", assert_hostname=False).request(method=method, url=url)


class Chemica:
    @staticmethod
    def solve(substance_1: str, substance_2: str) -> Union[List[Equation], Equation]:
        """
        The method gets chemical substances and finds solutions for them.
        :param substance_1: The first chemical substance.
        :param substance_2: The second chemical substance.
        :return: List of the equations or one equation.
        """
        response = _Request.make("GET", f"https://chemequations.com/ru/?s={substance_1}+%2B+{substance_2}")
        soup = BeautifulSoup(response.data, "html.parser")
        multiple_solutions = soup.find("table", {"class": "table possible-solutions center"})
        if multiple_solutions:
            equations = []
            for url in [url.get("href") for url in multiple_solutions.find("tbody").find_all("a")]:
                response = _Request.make("GET", f"https://chemequations.com/ru/{url}")
                soup = BeautifulSoup(response.data, "html.parser")
                equation = "".join([char.text.strip("\n").replace("\xa0", "").rstrip(" ") for char in
                                   soup.find_all("h1", {"class": "equation main-equation well"})])
                equations.append(Equation(substances=(substance_1, substance_2), result=equation))
            return equations
        else:
            equation = "".join([char.text.strip("\n").replace("\xa0", "").rstrip(" ") for char in
                                soup.find_all("h1", {"class": "equation main-equation well"})])
            return Equation(substances=(substance_1, substance_2), result=equation)

    @staticmethod
    def info(substance: str, language_code: str = "en") -> Substance:
        """
        This method returns base information about the chemical substance.
        :param substance: The chemical substance.
        :param language_code: Language code. By default, is EN.
        :return: Information about the chemical substance.
        """
        response = _Request.make("GET", f"https://chemequations.com/{language_code}/?s={substance}")
        soup = BeautifulSoup(response.data, "html.parser")
        information = soup.find("div", {"class": "panel panel-default equation-block"})
        return Substance(substance=substance, name=", ".join(name.text for name in information.find_all("em")[:-1]),
                         condition=information.find_all("li")[1].text.split(":")[1].strip(" "))
