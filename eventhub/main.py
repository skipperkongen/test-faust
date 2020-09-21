import faust
import os

from model import Greeting

BROKER_SERVER = os.environ.get('BROKER_SERVER')
BROKER_USERNAME = os.environ.get('BROKER_USERNAME')
BROKER_PASSWORD = os.environ.get('BROKER_PASSWORD')

app = faust.App(
    'hello-app',
    broker='kafka://kafka:9092',
    store='memory://'
)

topic = app.topic('hello', value_type=Greeting)

@app.agent(topic)
async def hello(greetings):
    async for greeting in greetings:
        print(f'Consumed greeting from {greeting.from_name} to {greeting.to_name}')
        #logger.info(f'Consumed greeting from {greeting.from_name} to {greeting.to_name}')

if __name__ == '__main__':
    app.main()
