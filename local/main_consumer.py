#import logging

import faust

from model import Greeting

#logger = logging.getLogger()

app = faust.App('hello-app', broker='kafka://kafka:9092')
topic = app.topic('hello', value_type=Greeting)

@app.agent(topic)
async def hello(greetings):
    async for greeting in greetings:
        print(f'Consumed greeting from {greeting.from_name} to {greeting.to_name}')
        #logger.info(f'Consumed greeting from {greeting.from_name} to {greeting.to_name}')

if __name__ == '__main__':
    app.main()
