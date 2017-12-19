from konlpy.tag import Mecab

def count(body):
    mecab = Mecab()
    if len(body) != 0:
        text = body[0].get_text()

        f = open("../keyword.txt", 'r')
        while True:
            line = f.readline()
            line = line.replace('\n', '')
            if not line: break
            text = text.replace(line, '부실')
        f.close()

        nouns = mecab.nouns(text)
        print(nouns.count('부실'))