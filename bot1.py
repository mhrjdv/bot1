from typing import Any
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Any = '6658164503:AAHh9Cjbsdsdsy5OyYXQ9CXlWh0NA1I'
BOT_USERNAME: Any = '@CU_QuickAccess_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('Hello, Welcome to Counting Unique Quick Access Bot')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('Hey, How can I help you ?')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('This is a special custom command')



# Response

def handle_response(text: str) -> str:

	processed: str = text.lower()

	if 'hello' in processed:
		return 'Hello there!'

	if 'bye' in processed:
		return 'Goodbye!'

	return 'Sorry, I don\'t understand you'

# Message

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
	message_type: str = update.message.chat.type
	text: str = update.message.text

	print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

	if message_type == 'group':
		if BOT_USERNAME in text:
			new_text: str = text.replace(BOT_USERNAME, '').strip()
			response: str = handle_response(new_text)
		else:
			return
	else:
		response: str = handle_response(text)

	print('Bot: ', response)
	await update.message.reply_text(response)




async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
	print(f'Update {update} caused error {context.error}')




if __name__ == '__main__':
	print('Starting bot...')
	app = Application.builder().token(TOKEN).build()

	# commands
	app.add_handler(CommandHandler('start', start_command))
	app.add_handler(CommandHandler('help', help_command))
	app.add_handler(CommandHandler('custom', custom_command))

	# messages
	app.add_handler(MessageHandler(filters.TEXT, message_handler))

	# errors
	app.add_error_handler(error)

	# polls the bot
	print('Polling...')
	app.run_polling(poll_interval=3)
