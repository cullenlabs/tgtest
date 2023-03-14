# pip install python-telegram-bot==12.0.0


import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler


TOKEN = "5122175911:AAHFXJv5NADoptZMtAdUJJtUOxRTPy4dbKg"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


from web3 import Web3

API_KEY = "VEAPRC4GI369EDZUEYEI34FPX3FPQBCXXC"
BASE_URL = "https://api.etherscan.io/api"
ETHER_VALUE = 10 ** 10
from web3 import Web3
import time 

infura_url = 'https://mainnet.infura.io/v3/ec6eddc050e34bca898c8f7a120d519f'
account = '0xef1c6e67703c7bd7107eed8303fbe6ec2554bf6b'
web3 = Web3(Web3.HTTPProvider(infura_url))

def confirmations(tx_hash):
    tx = web3.eth.get_transaction(tx_hash)
    return web3.eth.block_number - tx.blockNumber

def watch():
    while True:
        block = web3.eth.get_block('latest')
        print("Searching in block " + str(block.number))

        if block or block.transactions: 
            for transaction in block.transactions: 
                tx_hash = transaction.hex() # the hashes are stored in a hexBytes format
                tx = web3.eth.get_transaction(tx_hash)
                if tx.to != None:
                    if tx.to == account:
                        print("Transaction found in block {} :".format(block.number))
                        print({
                            "hash": tx_hash,
                            "from": tx["from"],
                            "value": web3.fromWei(tx["value"], 'ether')
                            })




if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
    watch()
