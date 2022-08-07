import os

from telethon import TelegramClient, events


api_id = int(os.getenv("api_id"))
api_hash = os.getenv("api_hash")
bot_token = os.getenv("bot_token")


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


def zelda(list):
	c = 1
	r = list.split(" ")
	z, d = r[-1].split(".rar")
	z = z[:-2]
	r = r[:-1]
	out = ""
	for i in r:
		if len(r) > 9:
			if c < 10:
				out += "[" + i + "]" + "@(" + z + "0" + str(c) + ".rar" + d + ")\n"
			else:
				out += "[" + i + "]" + "@(" + z + str(c) + ".rar" + d + ")\n"
		else:
			out += "[" + i + "]" + "@(" + z + "0" + str(c) + ".rar" + d + ")\n"
		c += 1
	return out


def start_filter(event):
	list_words_to_exclude = ["/start", "/Start"]
	for word in list_words_to_exclude:
		if word in event.raw_text:
			return False
	return True


with bot:
	@bot.on(events.NewMessage(pattern='^/start'))
	async def start(event):
		sender = await event.get_sender()
		await bot.send_message(event.sender_id, "Hola querid@ " + str(
			sender.username) + ", cuan grande es tu vagancia que necesitas un bot para crear Zeldas?")


	@bot.on(events.NewMessage(func=start_filter))
	async def code(event):
		if len(str(event.raw_text)):
			a = zelda(event.raw_text).splitlines()
			s = ""
			for f in a:
				n, z = f.split("@")
				s += n + z + "\n"
			await bot.send_message(event.sender_id, s, link_preview=False)

bot.start()
print("--------------------------------------------------------------------------")
bot.run_until_disconnected()
