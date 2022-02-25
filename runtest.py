import subprocess, os, time, json, argparse

# This will measure setup and teardown time

def getopts():
  parser = argparse.ArgumentParser(description='Run throughput test.')
  parser.add_argument('--all', help='path to runtime that acquires all cowns at once', required=True)
  parser.add_argument('--one', help='path to runtime that acquires one cown at a time', required=True)
  parser.add_argument('--repeats', type=int, default=100, help='number of times to repeat the runs')
  args = parser.parse_args()
  return args

if __name__ == "__main__":
    args = getopts()

    results = {"all": [], "one": []}
    for acquire in results.keys():
        for num in range(1, os.cpu_count() + 1):
            print(f"acquiring {acquire} with {num} cpus", end="", flush=True)
            total = 0
            for exp in range(args.repeats):
                start = time.time()
                subprocess.run([f"{getattr(args, acquire)}", "throughput-test.verona", f"--run-cores={num}", "--run"], check=True)
                end = time.time()
                total += (end - start)
                if exp % 10 == 0:
                    print(".", end="", flush=True)
            results[acquire].append(total / 100)
            print("done")

    with open("log", "w") as outfile:
      outfile.write(json.dumps(results, indent=2))
