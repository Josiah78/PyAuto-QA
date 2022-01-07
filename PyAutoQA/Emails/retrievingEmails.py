import imapclient
import pyzmail

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('josiahjamison08@gmail.com', 'paperplanes')
imapObj.select_folder('INBOX', readonly=True)
imapObj.search(['ALL'])

UIDs = imapObj.search(['ALL'])
rawMessages = imapObj.fetch[7], ['BODY']
message = pyzmail.PyzMessage.factory(rawMessages[7][b'BODY[]'])
message.get_subject()
message.get_address('from')
message.get_address('to')
UIDs
imapObj.select_folder('INBOX', readonly=False)
imapObj.delete_messages(UIDs)
imapObj.expunge()
imapObj.logout()