# Benchmark
Run a benchmark of 500 philospers trying to eat 500 times.
Compare two acquire methods, acquire all and acquire one cown and a time when spawning behaviours

# Build
`docker build -t benchmark .`

# Run
`docker run -v <path>:/output/ --rm --name dining-phils benchmark`
