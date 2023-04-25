# example/views.py
#
from datetime import datetime
#import telebot
import os

from django.http import HttpResponse

def index(request):
    token = os.environ['TOKEN']
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Verertererercel!</h1>
            <p>The current time is { now }.  Token: {token}</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
