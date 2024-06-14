import random

EATING = 'No i dont eat. I am not a human'
SLEEP = 'No i dont sleep'
RESPONSE1='Great!'
GREET='I\'m fine. how about yourself?'
GREET_RESPONSE1='I\'m pretty good. thanks for asking.Wby?'
RESPONSE_AGE='I don\'t have an age in the traditional sense since I\'m a chatbot.'
RESPONSE4='It was really nice talking to you also.'
RESPONSE6='I dont have likes or dislikes'
RESPONSE7='Dont worry! I am with you. You can share with me anything you want'
RESPONSE9='See you soon. Goodbye.'
CITY_RESPONSE1='i live in pasadena.'
CITY_RESPONSE2='it\'s in california.'
CITY_RESPONSE3='it\'s pretty big. It has about 3 million people.'
CITY_RESPONSE9='No, i don\'t have a car'
RESPONSE10='Yess, What can I do for you?'
RESPONSE11='Be with someone that doesn\'t think of you as an option, but as the single choice'
RESPONSE12='Dont get worried. Life is too short to argue so just let it go.'
RESPONSE13='Of course! What would you like to talk about? Whether it\'s sharing your day, discussing a topic, or asking questions, I\'m here to chat.'
RESPONSE14='As a Chatbot, I don\'t have access to real-time data, including weather forecasts. '
RESPONSE15='Certainly! What genre or type of movie are you in the mood for? Whether you\'re looking for action, comedy, drama, or something else, let me know your preferences, and I\'ll recommend a movie for you.'
RESPONSE16='For action movies, one classic recommendation is "Die Hard" (1988), starring Bruce Willis. It\'s a thrilling and iconic film set during a hostage situation in a Los Angeles skyscraper on Christmas Eve. Bruce Willis plays John McClane, a New York City cop who must single-handedly take on a group of terrorists led by Hans Gruber (played by Alan Rickman). "Die Hard" is known for its intense action sequences, memorable one-liners, and suspenseful plot. It\'s a must-watch for any action movie fan!'
RESPONSE17='You\'re welcome! If you have any more questions or need further recommendations, feel free to ask. Enjoy watching the movie!'
RESPONSE18='Great! If you ever need assistance in the future or just want to chat, don\'t hesitate to reach out. Have a wonderful day!'
RESPONSE19='Why don\'t you distract yourself by watching a movie'


def unknown():
    response = ['Could you please rephrase that?',
                'What does that mean',
                'Sorry i cant understand'][random.randrange(3)]
    return response