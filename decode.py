import os
import json
from bs4 import BeautifulSoup

def get_title(soup):
    title = soup.find("h4", class_="page-header").text.strip()
    return title

def get_tags(soup):
    tags_div = soup.find('div', {'class': 'col-md-3'})
    tags = [a.text.strip() for a in tags_div.find_all('a', {'class': 'btn btn-xs btn-default'})]
    return tags

def get_description(soup):
    descriptions = str(soup.find('h1', string='Description').find_parent('div', class_='panel panel-default').find('div', class_='panel-body')).find_all('p')
    description = ""
    for des in descriptions:
        des.text.strip()
    return description

def decode_html_to_json():
    problems = []
    filenames = os.listdir("./problems")
    filenames.sort(key=lambda name: int(name.split('problem')[1].split('.')[0]))
    for filename in filenames:
        with open(f"./problems/{filename}", "r") as file:
            soup = BeautifulSoup(file, "html.parser")
            title = get_title(soup)
            tags = get_tags(soup)

            problem = {
                "title": title,
                "tags": tags,
                "description": description,
                "input_format": input_format,
                "output_format": output_format,
                "samples": samples,
                "hints": hints,
                "problem_source": problem_source,
                "solution": solution,
                "subtasks": subtasks,
                "test_limits": test_limits
            }
            problems.append(problem)

    with open("problems.json", "w", encoding='UTF-8') as file:
        json.dump(problems, file, indent=4, ensure_ascii=False)

decode_html_to_json()