import MarkovChain

def main():
    mark = MarkovChain.MarkovChain()
    f = open("text.txt", "rb")
    text = f.read()
    f.close()
    mark.fit(text.split(b" "))
    print((b" ".join(mark.forward([b"hello,"], 1000))).decode("UTF-8"))

if __name__ == '__main__':
    main()