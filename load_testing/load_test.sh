# restricted
wrk -t50 -c2500 -d30s -s post.lua http://000.000.000.000:8000/predict --latency
