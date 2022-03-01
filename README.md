# Benchmark
Run a benchmark of 500 philospers trying to eat 500 times.
Compare two acquire methods, acquire all and acquire one cown and a time when spawning behaviours

# With Docker
## Build
```
docker build -t benchmark .
```

## Run
```
docker run -v <path>:/output/ --rm --name dining-phils benchmark
```

# Without Docker
## Clone verona repo and checkout PR with acquire all semantics
```
git clone --recursive  https://github.com/microsoft/verona.git
git fetch origin pull/528/head:acquire-all
git checkout acquire-all
```

## Build two compiler variants
Inside the verona repo:
```
mkdir build-acquire-one build-acquire-all
cd build-acquire-one
cmake ../ -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=clang++-8 -DCMAKE_C_COMPILER=clang-8 -DCMAKE_INSTALL_PREFIX=dist
ninja
cd ../build-acquire-all
cmake ../ -G Ninja -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_COMPILER=clang++-8 -DCMAKE_C_COMPILER=clang-8 -DCMAKE_INSTALL_PREFIX=dist -DACQUIRE_ALL=On
ninja
```

## Run the benchmark
```
python3 run-benchmark.py --all=<path-to-compiler-with-acquire-all> --one=<path-to-compiler-without-acquire-all> --repeat=<number-of-repeats>
```

## Optionally: plot a nice graph
```
python3 plot.py out.csv
```