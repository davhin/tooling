import sys
import modal

app = modal.App("my-example-app")


@app.function()
def f(i: int) -> float:
    if i % 2 == 0:
        print("hello", i)
    else:
        print("world", i, file=sys.stderr)
    return i**2


@app.local_entrypoint()
def main():
    # run this locally
    print(f.local(1000))

    # run this remotely
    print(f.remote(1000))

    # run this remote;y in parallel
    total = 0
    for ret in f.map(range(200)):
        total += ret
    print(total)
