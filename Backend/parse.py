import requests


response = requests.get('https://api.hh.ru/vacancies')

vacancies_list = []
vacancies = response.json()['items']
for vacancy in vacancies:
    title = vacancy['name']
    vacancies_list.append(title)


vacancies_id_list = []
for vacancy_id in vacancies:
    title = vacancy_id['id']
    vacancies_id_list.append(title)
    
salary_list = []



scedule_list = []
for scedule in vacancies:
    title = scedule['scedule']['name']
    scedule_list.append(title)

professional_roles_list = []
for professional_roles in vacancies:
    title = professional_roles['professional_roles']['name']
    professional_roles_list.append(title) 


employment_list = []
for employment in vacancies:
    title = employment['employment']['name']
    employment_list.append(title)

experience_list = []
for experience in vacancies:
    title = experience['experience']['name']
    experience_list.append(title)