import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import lxml
from re import sub as re_sub


# Немного информации об Иннополисе
class information_about_innopolis():

    # О городе иннополис
    def about_the_city_of_innopolis():
        url = 'https://apply.innopolis.university/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        city = soup.find('div', 'campus-info__inno-city')
        city_title = city.find('h2').text
        city_text = city.find('p').text

        return city_title + '\n' + city_text

    # О кампусе
    def about_campus():
        url = 'https://apply.innopolis.university/'
        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'Похоже с сервером какие-то неполадки, пожалуйста попробуйте перезапустить бота с помощью это команды /start'
        soup = BeautifulSoup(response.text, 'lxml')

        campus = soup.find('div', 'campus-info-entrants-left')
        campus_title = campus.find('h2').text
        campus_text = campus.find('p').text

        return re_sub('\s{2,}', ' ', campus_title) + '\n' + campus_text

    # О студенческой жизни
    def student_life():
        url = 'https://apply.innopolis.university/'
        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'Похоже с сервером какие-то неполадки, пожалуйста попробуйте перезапустить бота с помощью это команды /start'
        soup = BeautifulSoup(response.text, 'lxml')

        student = soup.find('div', 'campus-info__student-life')
        student_title = student.find('h2').text
        student_text = student.find('p').text

        return student_title + '\n' + student_text

    # Эта функция отвечает за информацию об обучении
    def about_study_parser():
        url = "https://apply.innopolis.university/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"
        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'Похоже с сервером какие-то неполадки, пожалуйста попробуйте перезапустить бота с помощью это команды /start'
        soup = BeautifulSoup(response.text, 'lxml')
        list_of_training_information = soup.find_all("div", class_="three-card-slider-description-item__content")
        list_cards = ''

        # Перебераем все карточки с информацией с банера об учебе в иннополисе на главной странице
        for information_card in list_of_training_information:
            card_title = information_card.find("h5", class_="three-card-slider-description-item-title").text
            card_text = information_card.find("p", class_="three-card-slider-description-item-text").text
            list_cards += card_title + ':\n' + re_sub('\s{2,}', ' ', card_text) + '\n\n'

        return list_cards

    # как поступить (ЭТО НЕ ТОЛЬКО ДЛЯ АСПИРАНТУРЫ, А ДЛЯ ВСЕГО)
    def how_to_go():
        url = 'https://apply.innopolis.university/postgraduate-study/'
        ua = UserAgent()

        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'проблемы с сервером'

        soup = BeautifulSoup(response.text, 'lxml')

        # переменная для хранения всех шагов для поступления
        all_steps = ''

        # блок как поступить
        how_to_go_div = soup.find('div', {'class': 'block-wrapper block-columns-three-cards'})

        # все шаги для поступления
        steps = how_to_go_div.find_all('div', {'class': 'three-cards__card'})
        for num, step in enumerate(steps, 1):
            # что делать
            action = step.find('h3', {'class': 'card__title'}).text.lower().capitalize().strip()
            # подробное описание
            description = step.find('div', {'class': 'card__subtitle'}).text.strip()
            # объединяем
            full_how_to_go = f'{str(num)}. {action}:\n{description}\n\n'
            # добавляем к имеющимся шагам
            all_steps += full_how_to_go

        return all_steps


class postgraduate_studies():

    # направление подготовки
    def direction_preparation():
        url = 'https://apply.innopolis.university/postgraduate-study/'
        ua = UserAgent()

        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'Похоже с сервером какие-то неполадки, пожалуйста попробуйте перезапустить бота с помощью это команды /start'

        soup = BeautifulSoup(response.text, 'lxml')

        # блок направление подготовки
        direction_preparation_div = soup.find('div',
                                              {'class': 'block-wrapper block-separator-mainviewport-after-block'}).find(
            'div', {'class': 'mainviewport-after-block__main'})

        # заголовок
        direction_preparation_title = direction_preparation_div.find('h3').text
        # контент
        direction_preparation_content = re_sub('\s{2,}', ' ', direction_preparation_div.find('div').text.capitalize())
        # объединяем в переменную для хранения направления подготовки
        all_direction = f'{direction_preparation_title}:\n{direction_preparation_content}'

        return all_direction

    # структура обучения
    def education_schema():
        url = 'https://apply.innopolis.university/postgraduate-study/'
        ua = UserAgent()

        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'Похоже с сервером какие-то неполадки, пожалуйста попробуйте перезапустить бота с помощью это команды /start'

        soup = BeautifulSoup(response.text, 'lxml')

        # переменная для хранения всей структуры обучения
        all_schema = ''

        # блок стрктура обучения
        education_schema_div = soup.find('div', {'class': 'block-wrapper block-columns-two-cards'})

        # все компоненты структуры
        parts = education_schema_div.find_all('div', {'class': 'two-cards__card'})
        for num, part in enumerate(parts, 1):
            # название
            component = part.find('h3', {'class': 'card__title'}).text.lower().capitalize().strip()
            # подробное описание
            list_description = part.find('div', {'class': 'landing-node-text'}).find_all('li', {'class': 'card__li'})
            description = '\n'.join(['—' + elem.text.strip() for elem in list_description])
            # объединяем
            full_schema = f'{str(num)}. {component}:\n{description}\n\n'
            # добавляем к имеющейся части структуры
            all_schema += full_schema

        return all_schema

    # учебные программы
    def learning_programs():
        url = 'https://apply.innopolis.university/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit'
        ua = UserAgent()

        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'Похоже с сервером какие-то неполадки, пожалуйста попробуйте перезапустить бота с помощью это команды /start'

        soup = BeautifulSoup(response.text, 'lxml')

        # блок с учебными программами
        learning_programs_div = soup.find('div', {'class': 'block-wrapper block-learning-programs'}).find('div', {
            'class': 'learning-program graduate-school'})

        # контент
        all_learning_programs = learning_programs_div.find('div').text

        return all_learning_programs


class magistr():

    # направление подготовки
    def direction_preparation():
        url = 'https://apply.innopolis.university/master/datascience/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit'
        ua = UserAgent()

        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'Похоже с сервером какие-то неполадки, пожалуйста попробуйте перезапустить бота с помощью это команды /start'

        soup = BeautifulSoup(response.text, 'lxml')

        # заголовок
        direction_preparation_title = list(filter(lambda elem: elem,
                                                  re_sub('ии', 'и и', soup.find("div", {
                                                      "class": "main-page__main-viewport-titles"}).text).split('\n')))[
            1]
        # контент
        direction_preparation_content = soup.find("div", class_="events__event-info__subtitle").text

        # объединяем
        all_direction = f'{direction_preparation_title}:\n{direction_preparation_content}'

        return all_direction

    # структура обучения
    def education_schema():
        url = 'https://apply.innopolis.university/master/datascience/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit'
        ua = UserAgent()

        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'Похоже с сервером какие-то неполадки, пожалуйста попробуйте перезапустить бота с помощью это команды /start'

        soup = BeautifulSoup(response.text, 'lxml')

        # переменная для хранения всей структуры обучения
        all_schema = ''

        # все компоненты структуры
        parts = soup.find("div", class_="learning-programs-wrap").find_all('div', {'class': 'learning-program'})[1:]
        for part in parts:
            # название
            component = part.find("h5").text.capitalize().strip()
            # подробное описание
            description = re_sub('•', '\n•',
                                 re_sub('\n', ' ', part.find("div",
                                                             class_="learning-program-description").text)).strip().capitalize()
            # объединяем
            full_schema = f'{component}:\n{description}\n\n'
            # добавляем к имеющейся части структуры
            all_schema += full_schema

        return all_schema

    # учебные программы
    def learning_programs():
        url = 'https://apply.innopolis.university/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit'
        ua = UserAgent()

        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'Похоже с сервером какие-то неполадки, пожалуйста попробуйте перезапустить бота с помощью это команды /start'

        soup = BeautifulSoup(response.text, 'lxml')

        # блок с учебными программами
        learning_programs_div = soup.find('div', {'class': 'block-wrapper block-learning-programs'}).find('div', {
            'class': 'learning-program master'})

        # контент
        all_learning_programs = '\n'.join([elem.text for elem in learning_programs_div.find_all('p')])

        return all_learning_programs


class bakalavr():

    # структура обучения
    def education_schema():
        url = "https://apply.innopolis.university/bachelor/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"
        ua = UserAgent()

        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'проблемы с сервером'

        soup = BeautifulSoup(response.text, 'lxml')

        # переменная для хранения всей структуры обучения
        all_schema = ''

        # все компоненты структуры
        parts = soup.find("div", class_="learning-programs-wrap").find_all('div', {'class': 'learning-program'})[1:]
        for part in parts:
            # название
            component = part.find("h5").text.capitalize().strip()
            # подробное описание
            description = re_sub('•', '\n•',
                                 re_sub('\n', ' ', part.find("div",
                                                             class_="learning-program-description").text)).strip().capitalize()
            # объединяем
            full_schema = f'{component}:\n{description}\n\n'
            # добавляем к имеющейся части структуры
            all_schema += full_schema

        return all_schema

    # учебные программы
    def learning_programs():
        url = 'https://apply.innopolis.university/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit'
        ua = UserAgent()

        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'проблемы с сервером'

        soup = BeautifulSoup(response.text, 'lxml')

        # блок с учебными программами
        learning_programs_div = soup.find('div', {'class': 'block-wrapper block-learning-programs'}).find('div', {
            'class': 'learning-program undergraduate'})

        # контент
        all_learning_programs = '\n'.join(
            list(filter(lambda elem: elem, [elem.text for elem in learning_programs_div.find_all('p')]))
        )

        return all_learning_programs

    # направление подготовки
    def direction_preparation():
        url = "https://apply.innopolis.university/bachelor/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"
        ua = UserAgent()

        try:
            response = requests.get(url, headers={'User-Agent': ua.random}, timeout=3)
        except TimeoutError:
            return 'проблемы с сервером'

        soup = BeautifulSoup(response.text, 'lxml')

        # заголовок
        direction_preparation_title = soup.find("h3", {"class": "mainviewport-after-block__main-title"}).text
        # контент
        direction_preparation_content = soup.find("div", {"class": "mainviewport-after-block__main-subtitle"}).text

        # объединяем
        all_direction = f'{direction_preparation_title}:\n{direction_preparation_content}'

        return all_direction
