from bs4 import BeautifulSoup
import requests

#Немного информации об Иннополисе
class information_about_innopolis():
    # О городе иннополис
    def about_the_city_of_innopolis():
        url = 'https://apply.innopolis.university/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features='html.parser')

        city = soup.find('div', 'campus-info__inno-city')
        city_title = city.find('h2').text
        city_text = city.find('p').text

        return city_title + '\n' + city_text


    # О кампусе
    def about_campus():
        url = 'https://apply.innopolis.university/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features='html.parser')

        campus = soup.find('div', 'campus-info-entrants-left')
        campus_title_bad = campus.find('h2').text
        campus_text = campus.find('p').text

        return campus_title_bad.replace('                ', '') + '\n' + campus_text


    # О студенческой жизни
    def student_life():
        url = 'https://apply.innopolis.university/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features='html.parser')

        student = soup.find('div', 'campus-info__student-life')
        student_title = student.find('h2').text
        student_text = student.find('p').text

        return student_title + '\n' + student_text


    # Эта функция отвечает за информацию об обучении
    def about_study_parser():
        url = "https://apply.innopolis.university/?lang=ru&id=12&site=s1&template=university24&landing_mode=edit"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features='html.parser')
        list_of_training_information = soup.find_all("div", class_="three-card-slider-description-item__content")
        list_cards = ''

        # Перебераем все карточки с информацией с банера об учебе в иннополисе на главной странице
        for information_card in list_of_training_information:
            card_title = information_card.find("h5", class_="three-card-slider-description-item-title").text
            card_text = information_card.find("p", class_="three-card-slider-description-item-text").text
            list_cards += card_title + ':\n' + card_text.replace("            ", "") + '\n\n'

        return list_cards
