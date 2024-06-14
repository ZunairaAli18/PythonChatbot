import re 
import long_responses as long

def message_probability(user_message, recognised_words,single_response=False, required_words=[]):
    message_certainty=0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty+=1

    percentage=float(message_certainty)/float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0    
    
def check_All_messages(message):
    highest_prob_list={}

    def response(bot_response,list_of_words,single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_probability(message,list_of_words,single_response,required_words)
        if isinstance(bot_response, list):
            bot_response = ' '.join(bot_response)
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
     #Responses-----------------------------------------------------------
    response('Hello!',['hello','hi','sup','hey','heyo'],single_response=True)
    response(long.GREET,['how','are','you','doing'],required_words=['how','doing'])
    response(long.RESPONSE1,['i','am','also','good'],required_words=['i','good'])
    response(long.SLEEP,['do','you','sleep'],required_words=['you','sleep'])
    response('Thank You!',['i','love','this','chatbot'],required_words=['love','this','chatbot'])
    response('Han Khaonga',['chamat','khayega'],required_words=['chamat'])
    response(long.EATING,['would','you','like','to','eat','something'],required_words=['you','eat'])
    response(long.RESPONSE_AGE,['what\'s','your','age'],required_words=['age'])
    response(long.GREET_RESPONSE1,['sup'],required_words=['sup'])
    response(long.RESPONSE4,['it','was','nice','talking','to','you'],required_words=['nice','talking','to','you'])
    response(long.RESPONSE6,['what\'s','your','favourite','color'],required_words=['your','favourite','color'])
    response(long.CITY_RESPONSE1,['where','do','you','live'],required_words=['you','live'])
    response(long.CITY_RESPONSE2,['where','is','pasadena'],required_words=['where','pasadena'])
    response(long.CITY_RESPONSE3,['how','much','big','it','is'],required_words=['how','much','big'])
    response(long.CITY_RESPONSE9,['do','you','have','a','car'],required_words=['you','have','car'])
    response(long.RESPONSE10,['oh','okay','okay'],required_words=['okay'])
    response(long.RESPONSE7,['i','am','feeling','sad','today'],required_words=['i','sad'])
    response(long.RESPONSE12,['i','think','i','am','confused'],required_words=['i','confused'])
    response(long.RESPONSE19,['yeah','you','are','right'],required_words=['yeah','you','are','right'])
    response(long.RESPONSE15,['can','you','suggest','me','a','movie'],required_words=['suggest','movie'])
    response(long.RESPONSE16,['action'],required_words=['action'])
    response(long.RESPONSE17,['thank','you','so','much'],required_words=['thank','you'])
    response(long.RESPONSE18,['sure'],required_words=['sure'])
    response(long.RESPONSE9,['okay','bye'],required_words=['bye'])
    best_match=max(highest_prob_list,key=highest_prob_list.get)
    if(highest_prob_list[best_match]<1):
        return long.unknown()
    else:
        return best_match



def get_response(user_input):
    split_message=re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response_bot = check_All_messages(split_message)  
    
    return response_bot
while True:
    print("Bot:" , get_response(input("You: ")))