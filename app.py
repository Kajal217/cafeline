import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAaLClAZCuY8BAGE2ZCADcFw99ymC745ElmEZClxaykhSxZCtetfZCoTPfQiDf4ZA776yHC6AG7qXm2nUqhza6uIBvZAUSPB1WNdWim1ZBqszADgnoMPVAK9ZAOdi89WklRpLrRi3ZCK9pHs6OzKYRdWZCXaNtV5s5jUPu7CXt4mDC5LnBZC04QYEcjA'
VERIFY_TOKEN = 'THISIS217REALLYHARDtothink217OFBECAUSEIDONTREALLY217GETwhatIam217doInG'
bot = Bot(ACCESS_TOKEN)


# We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        response_sent_text = get_message(message['message'])
                        send_message(recipient_id, response_sent_text)
                    # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_nontext_message()
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


# chooses a random message to send to the user
def get_message(message):
    for match in message:
        if "hours" in message:
            return ("We are open 7 days a week from 10am-6pm.")
        if "open" in message:
            return ("We are open 7 days a week from 10am-6pm.")
        elif "location" in message:
            return ("We are located on the downtown mall in Charlottesville, VA.")
        elif "where" in message:
            return ("We are located on the downtown mall in Charlottesville, VA.")
        else:
            return ("Someone will be in touch soon! Thanks for your interest in Cafeline")



def get_nontext_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    return random.choice(sample_responses)

# uses PyMessenger to send response to user
def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


if __name__ == "__main__":
    app.run()