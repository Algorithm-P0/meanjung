import re
def solution(m, musicinfos):
    m = m.replace('A#', 'H')
    m = m.replace('C#', 'I')
    m = m.replace('D#', 'J')
    m = m.replace('F#', 'K')
    m = m.replace('G#', 'L')
    checkM = m
    ansTime = 0
    ansTitle = None
    for music in musicinfos:
        s, e, title, code = music.split(",")
        code = code.replace('A#', 'H')
        code = code.replace('C#', 'I')
        code = code.replace('D#', 'J')
        code = code.replace('F#', 'K')
        code = code.replace('G#', 'L')

        h, m = s.split(':')
        sh = int(h)*60
        sm = int(m)
        st = sh + sm
        h, m = e.split(':')
        eh = int(h)*60
        em = int(m)
        et = eh + em
        time = et - st
        if time <= len(code):
            if checkM in code[:time] and ansTime < time:
                ansTitle = title
                ansTime = time
        else:
            new_code = ''
            for i in range(time):
                new_code += code[i % len(code)]
            if checkM in new_code and ansTime < time:
                ansTitle = title
                ansTime = time
    if ansTitle is None:
        return '(None)'
    else:
        return ansTitle
