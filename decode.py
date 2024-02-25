import os
import json
from bs4 import BeautifulSoup

def lines_to_string(lines):
    return "".join([str(line) for line in lines])

def get_serial_number(soup):
    serial_number = soup.find("h4", class_="page-header").text.strip()
    serial_number = serial_number.split(" . ")[0]
    return serial_number

def get_title(soup):
    title = soup.find("h4", class_="page-header").text.strip()
    title = title.split(" . ")[1]
    return title

def get_tags(soup):
    tags_div = soup.find('div', {'class': 'col-md-3'})
    tags = [a.text.strip() for a in tags_div.find_all('a', {'class': 'btn btn-xs btn-default'})]
    return tags

def get_description(soup):
    description_HTMLs = soup.find('h1', string='Description').find_parent('div', class_='panel panel-default').find('div', class_='panel-body').contents
    description = lines_to_string(description_HTMLs).strip()
    return description

def get_input_format(soup):
    input_formats = soup.find('h1', string='Input Format').find_parent('div', class_='panel panel-default').find('div', class_='panel-body').contents
    input_format = lines_to_string(input_formats).strip()
    return input_format

def get_output_format(soup):
    output_formats = soup.find('h1', string='Output Format').find_parent('div', class_='panel panel-default').find('div', class_='panel-body').contents
    output_format = lines_to_string(output_formats).strip()
    return output_format

def get_samples(soup):
    samples = []
    sample_divs = soup.find_all('div', {'class': 'panel-body code-input copy-group-code'})
    temp_input = ""
    for i, sample_div in enumerate(sample_divs):
        if(i % 2 == 0):
            temp_input = sample_div.text.strip()
        else:
            sample = {
                temp_input: sample_div.text.strip()
            }
            samples.append(sample)
    return samples

def get_hints(soup):
    hints = str(soup.find('h1', string='Hints').find_parent('div', class_='panel panel-default').find('div', class_='panel-body')).strip()
    return hints

def get_problem_source(soup):
    problem_sources = soup.find('h1', string='Problem Source').find_parent('div', class_='panel panel-default').find('div', class_='panel-body')
    problem_source = lines_to_string(problem_sources.contents).strip()
    if problem_source == "":
        problem_source = None
    return problem_source

def get_solution(soup):
    try:
        solutions = soup.find('h1', string='Solution (Click to toggle)').find_parent('div', class_='panel panel-default').find('div', class_='panel-body hidden')
    except AttributeError:
        solution = None
        return solution
    solution = lines_to_string(solutions.contents).strip()
    return solution

def get_subtasks(soup):
    subtasks = str(soup.find('h1', string='Subtasks').find_parent('div', class_='panel panel-default').find('table', class_='table table-hover table-striped table-condensed')).strip()
    return subtasks

def get_test_limits(soup):
    test_limits = str(soup.find('div', id='collapseLimit')).strip()
    return test_limits

def decode_html_to_json():
    problems = []
    filenames = os.listdir("./problems")
    filenames = [name for name in filenames if '.html' in name]
    filenames.sort(key=lambda name: int(name.split('problem')[1].split('.')[0]))
    for filename in filenames:
        with open(f"./problems/{filename}", "r", encoding='utf-8') as file:
            soup = BeautifulSoup(file, "html.parser")
            serial_sumber = get_serial_number(soup)
            title = get_title(soup)
            tags = get_tags(soup)
            description = get_description(soup)
            input_format = get_input_format(soup)
            output_format = get_output_format(soup)
            samples = get_samples(soup)
            hints = get_hints(soup)
            problem_source = get_problem_source(soup)
            solution = get_solution(soup)
            subtasks = get_subtasks(soup)
            test_limits = get_test_limits(soup)

            problem = {
                "serial_number": serial_sumber,
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

    with open("./problems/problems.json", "w", encoding='UTF-8') as file:
        json.dump(problems, file, indent=4, ensure_ascii=False)

decode_html_to_json()