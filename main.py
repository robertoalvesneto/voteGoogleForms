from googleforms.bot_forms import BotForms


if __name__ == "__main__":
    bf = BotForms()

    website_url = "https://forms.gle/rUd5fBs5CPJv5ML29"
    name_title_field = "Resposta curta"
    insert_text = "texto aleatorio a ser inserido"

    bf.builder(website_url, name_title_field, insert_text)
