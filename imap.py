import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('liuxun931@gmail.com', 'lx061511')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.