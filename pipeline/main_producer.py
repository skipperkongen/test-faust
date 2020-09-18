#import logging

import faust

from model import Greeting

#logger = logging.getLogger()

app = faust.App('hello-app', broker='kafka://kafka:9092')
topic = app.topic('hello', value_type=Greeting)

@app.timer(interval=1.0)
async def example_sender(app):
    greeting = Greeting(from_name='Cronjay', to_name='you')
    await topic.send(
        value=greeting,
    )
    #logger.info(f'Produced greeting from {greeting.from_name} to {greeting.to_name}')
    print(f'Produced greeting from {greeting.from_name} to {greeting.to_name}')


if __name__ == '__main__':
    app.main()
