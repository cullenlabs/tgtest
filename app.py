# pip install python-telegram-bot==12.0.0


from email import message
import telebot
import requests

bot = telebot.TeleBot("5122175911:AAHFXJv5NADoptZMtAdUJJtUOxRTPy4dbKg")
chave = 'a526c22f'




def check(message):
    with open ("usuarios/usuarios.txt", "r") as usuarios:
        usuarios = usuarios.read().split()
        if message.from_user.username.strip() in usuarios:
            return True


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f"Olá sou um robô Telegram! {message.from_user.username}")



def extract(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['filme', 'filmes'])
def busca_movie(message):
    if check(message):
    	
        movie = extract(message.text)
        url_base = f'http://www.omdbapi.com/?apikey={chave}&t={movie}&plot=full'
        response = requests.get(url_base).json()
        
        if response["Response"] == "True":
            text = (
                   f"Filme: {response['Title']}\n"
                   f"Data de lançamento: {response['Released']}\n"
                   f"Diretor(es): {response['Director']}\n"
                   f"Escritor(es): {response['Writer']}\n"
                   f"Atores: {response['Actors']}.\n"
                   f"Enredo: {response['Plot']}\n"
                   f"Gênero: {response['Genre']}\n"
                   f"Link para o pôster do filme: {response['Poster']}\n"
           )
        else:
            text = "Desculpe. Filme não encontrado"

        bot.reply_to(message, text)
    else:
        bot.reply_to(message, f"O nome de usuario {message.from_user.username} nao esta aprovado")


@bot.message_handler(commands=['cep'])
def cep(message):
    if check(message):

        cep_ = extract(message.text)  # retorna uma lista
        
        cep_ok = cep_[0]
        if len(cep_ok) == 8:
            
            url_base = f'https://viacep.com.br/ws/{cep_ok}/json/'
            print(cep_ok)
            r = requests.get(url_base).json()
            #print(r)
        else:
            print(cep_ok)
            r = {'logradouro':"CEP Não encontrado"}
        text="A rua é : "+r['logradouro']
        bot.reply_to(message, text)
    else:
        bot.reply_to(message, f"O nome de usuario {message.from_user.username} nao esta aprovado")
        
@bot.message_handler(commands=['caps'])
def caps(message):
    if check(message):
        text_caps = ' '.join(extract(message.text)).upper()
        bot.reply_to(message, text_caps)
    else:
        bot.reply_to(message, f"O nome de usuario {message.from_user.username} nao esta aprovado")

@bot.message_handler(commands=['cot'])    
def cot(message):
    if check(message):
        ativo = extract(message.text)
        ativo = ativo[0]  # retorna uma lista
        try:
            url_base = f'https://www.mercadobitcoin.net/api/{ativo}/ticker/'
            r = requests.get(url_base).json()
            text=str(r)
        except:
            text = "Use uma moeda valida"
        bot.reply_to(message, text)
    else:
        bot.reply_to(message, f"O nome de usuario {message.from_user.username} nao esta aprovado")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if check(message):
        bot.reply_to(message, message.text)
    else:
        bot.reply_to(message, f"O nome de usuario {message.from_user.username} nao esta aprovado")
          

bot.infinity_polling()
