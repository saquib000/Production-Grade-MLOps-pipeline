# restricted
wrk -t50 -c2500 -d30s -s post.lua http://136.111.190.138:8000/predict --latency
