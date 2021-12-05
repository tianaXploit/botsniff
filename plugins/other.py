from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

@Client.on_message(filters.command("start"))
async def start_msg(client, message):
	await message.reply_text(
		f"Hi {message.from_user.mention}, I am Bot decrypt httpcustom only.\n\nClick Help button to know how to use.",
		reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🌕 Help", callback_data=f"help"),
					InlineKeyboardButton("🌑 About", callback_data=f"about")
				]]
			),
		quote=True)

@Client.on_callback_query()
async def cb_handler(client, update):
	cb_data = update.data
	
	if "help" in cb_data:
		await update.message.edit_text("please clik link for actived bot\nhttps://ouo.io/FXEBrhg\ntutorial\nhttps://t.me/decrypthttpcustum/4",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🌑 About", callback_data=f"about"),
					InlineKeyboardButton("🔙 Back", callback_data=f"back")
				]]
			))
	elif "about" in cb_data:
		await update.message.edit_text("Language: JavaScript",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🌕 Help", callback_data=f"help"),
					InlineKeyboardButton("🔙 Back", callback_data=f"back")
				]]
			))
	elif "back" in cb_data:
		await update.message.edit_text(f"Hi {update.from_user.mention}, I am Bot decrypt httpcustom only.\n\nClick Help button to know how to use.",
			reply_markup=InlineKeyboardMarkup(
				[[
					InlineKeyboardButton("🌕 Help", callback_data=f"help"),
					InlineKeyboardButton("🌑 About", callback_data=f"about")
				]]
			))


