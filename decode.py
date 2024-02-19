import os
import json
from bs4 import BeautifulSoup

def decode_html_to_json():
    problems = []
    filenames = os.listdir("./problems")
    filenames.sort(key=lambda name: int(name.split('problem')[1].split('.')[0]))
    for filename in filenames:
        with open(f"./problems/{filename}", "r") as file:
            soup = BeautifulSoup(file, "html.parser")
            title = str(soup.find('h4', class_='page-header').text)
            tags = []
            for tag in soup.find('div', class_='col-md-3').find_all('a', class_='btn btn-xs btn-default'):
                tags.append(str(tag.text))
            description = None
            input_format = None
            output_format = None
            samples = []
            hints = None
            problem_source = None
            solution = None
            subtasks = None
            test_limits = None

            try:
                description = str(soup.find('h1', string='Description').find_parent('div', class_='panel panel-default').find('div', class_='panel-body'))
            except AttributeError:
                pass

            try:
                input_format = str(soup.find('h1', string='Input Format').find_parent('div', class_='panel panel-default').find('div', class_='panel-body'))
            except AttributeError:
                pass

            try:
                output_format = str(soup.find('h1', string='Output Format').find_parent('div', class_='panel panel-default').find('div', class_='panel-body'))
            except AttributeError:
                pass

            try:
                for sample in soup.find_all('div', class_='panel panel-default copy-group problem-copy-group'):
                    samples.append(str(sample.find('div', class_='panel-body code-input copy-group-code').text))
            except AttributeError:
                pass

            try:
                hints = str(soup.find('h1', string='Hints').find_parent('div', class_='panel panel-default').find('div', class_='panel-body'))
                if hints == "<div class=\"panel-body\">\n</div>":
                    hints = None
            except AttributeError:
                pass

            try:
                problem_source = str(soup.find('h1', string='Problem Source').find_parent('div', class_='panel panel-default').find('div', class_='panel-body').text)
            except AttributeError:
                pass

            try:
                solution = str(soup.find('h1', string='Solution (Click to toggle)').find_parent('div', class_='panel panel-default').find('div', class_='panel-body hidden'))
            except AttributeError:
                pass

            try:
                subtasks = str(soup.find('h1', string='Subtasks').find_parent('div', class_='panel panel-default').find('table', class_='table table-hover table-striped table-condensed'))
            except AttributeError:
                pass

            try:
                test_limits = str(soup.find('i', class_='indicator glyphicon glyphicon-chevron-up pull-right').find_parent('div', class_='panel panel-default').find('div', class_='collapse in'))
            except AttributeError:
                pass

            problem = {
                "title": title.replace('\n', ''),
                "tags": tags,
                "description": description,
                "input_format": input_format,
                "output_format": output_format,
                "samples": samples,
                "hints": hints,
                "problem_source": problem_source.replace('\n', ''),
                "solution": solution,
                "subtasks": subtasks,
                "test_limits": test_limits
            }
            problems.append(problem)

    with open("problems.json", "w", encoding='UTF-8') as file:
        json.dump(problems, file, indent=4, ensure_ascii=False)

decode_html_to_json()