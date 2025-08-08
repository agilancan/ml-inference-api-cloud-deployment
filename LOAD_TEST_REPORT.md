## Local Testing:
Baseline: 1 user, 60 seconds:
- Response times: 27.58 ms
- Failure rates: 0
- Throughput per scenario: 0.3 RPS

Normal: 10 users, 5 minutes:
- Response times: 45.48 ms
- Failure rates: 0
- Throughput per scenario: 3.2 RPS


## Cloud Testing:
Baseline: 1 user, 60 seconds:
- Response times: 85.1 ms
- Failure rates: 0
- Throughput per scenario: 0.3 RPS

Normal: 10 users, 5 minutes:
- Response times: 83.69 ms
- Failure rates: 0
- Throughput per scenario: 3.2 RPS

Stress: 50 users, 2 minutes:
- Response times: 76.18 ms
- Failure rates: 0
- Throughput per scenario: 16.1 RPS

Spike: Ramp from 1 to 100 users over 1 minute:
- Response times: 75.34 ms
- Failure rates: 0
- Throughput per scenario: 28.2 RPS


## Bottlenecks:
From my locust tests, the cloud version of the app was a little slower than the local version. From my research, this is normal because the cloud has to deal with internet delays and sometimes cold starts, which happen when the system has to start a new server from scratch. The throughput, or requests per second (RPS), scaled in an efficient way I think again from what I looked up, about 0.3 RPS with 1 user, 3.2 RPS with 10 users, 16 RPS with 50 users, and 28 RPS with 100 users. This shows the system can handle more users without breaking or slowing down too much. I did not see problems with the model loading or memory during these tests, but those could appear with bigger or more complex requests. From my reserach, the similar response times at high loads suggest autoscaling is working well, but I haven’t yet pushed the system to its breaking point. Out of curiosity I wanted to push to 1000 and 10,000 users over 60s to see if it would handle it or break it, but was scared of incuring a lot of GCP related costs due to all the requests. I set my Cloud run setting to charge me by requests, so didn't feel comfortable pushing the system too much.


## Recommendations:
To keep performance strong, we can let Cloud Run autoscale so it adds more servers when traffic grows. We can also set a few servers to stay running all the time to avoid cold starts. If we want to find deeper bottlenecks, we could test with larger payloads, more users, or longer test times to check for slowdowns in the model or data handling. Watching throughput trends in future tests can also help spot if scaling starts to level off, which might mean a CPU, memory, or network limit is being hit.