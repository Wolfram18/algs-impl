# Codenrock New Year Code Battle
Решение 15 задач на алгоритмы по мотивам IT сериалов в рамках соревнования: "Codenrock New Year Code Battle".  
<https://codenrock.com/contests/codenrock-new-year-code-battle/>

1. [Алфавит](#алфавит)

## Алфавит
### Задание
Зашифруйте сообщение меняя буквы на их порядковый номер в алфавите. Пробелы при этом не учитывать. Строки будут даны без знаков препинания, только с пробелами. Регистр не учитывать.  

**Входные данные:** шифруемая строка, длиной до 1000 символов, на латинице  
**Пример входных данных:** MR Robot  
**Выходные данные:** через запятую порядковый номер букв в алфавите  
**Пример выходных данных:** 13,18,18,15,2,15,20  

### Код (alphabet.py)
```python
import sys
import string

def main():
    alphabet = string.ascii_lowercase  # латинский алфавит
    for line in sys.stdin:  # get input strings one by one
        line = line.replace(" ", "").rstrip()
        ind_list = [alphabet.find(x) + 1 for x in line.lower()]
        print(','.join(map(str, ind_list)))

if __name__ == '__main__':
    main()
```
