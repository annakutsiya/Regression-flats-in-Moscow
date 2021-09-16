with open ('referat.txt', 'r', encoding='utf-8') as f:
    file_len = 0
    text =''  
    for l in f:   
        file_len += len(l)
        text += l.strip() + ' '
    almost_words_list = []
    words = text.split(' ')
    for w in words:
       if w != '':
           almost_words_list.append(w)
    words_amount = len(almost_words_list)
    new_text = text.replace('.', '!')
    with open ('referat2.txt', 'w', encoding= 'utf-8') as new_f:
        new_f.write(f'Длина строки: {file_len}\nКоличество слов: {words_amount}\nИзменённый текст: {new_text}')




   