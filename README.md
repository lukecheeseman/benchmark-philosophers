# Benchmark
Run a benchmark of 1000 philospers trying to eat 1000 times.
Compare two acquire methods, acquire all and acquire one cown and a time when spawning behaviours

# Build
docker build -t benchmark .

# Run
docker run -v pwd:/output/ benchmark
