# Testing Faust

Faust is a Python framework creating Kafka apps. I've tested it.

|Test|Conclusion|
|-|-|
|Local Kafka|Works :-)|
|Eventhubs|Does not work ;-(|

## How to run

Run Faust with local Kafka (works):

```
make local_up
make local_down
```

Run Faust with Eventhubs (does NOT work):

```
make eventhub_up
make eventhub_down
```
