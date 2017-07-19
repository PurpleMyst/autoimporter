# autoimporter

Are your hands too tired from having to type `import` too many times? Well
then, this is the module for you!

Let's assume you have a file named `whywouldyoudothis.py` with the following
contents:

```python
def main():
    print(math.sqrt(25))


if __name__ == "__main__":
    main()
```

There's just two simple steps to utilize `autoimporter`, then!  
First, change `whywouldyoudothis.py` to have `# coding=autoimporter` at the
top, like so:

```python
# coding=autoimporter


def main():
    print(math.sqrt(25))


if __name__ == "__main__":
    main()
```

Then, just run your script with the included run.py script

```shell
python3 run.py whywouldyoudothis.py
```

It's as simple as riding a bike through a ring of fire! :)
