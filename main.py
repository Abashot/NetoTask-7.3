import os
from pprint import pprint

new_text = []

def count_lines(directory):
    file_list = os.listdir(directory)
    
    for file in file_list:
        with open(directory + '/' + file, 'r', encoding='utf-8') as f:
            count = 0
            text = ''  
            
            for line in f:
                count += 1
                text += line
                
            new_text.append({'filename': file, 'lenght': count, 'text': text})

def write_new_file():
    count_lines('text files')
    
    with open('new_txt', 'w', encoding='utf-8') as nf:
        new_text.sort(key=lambda file_list: file_list['lenght'])
        
        for dict in new_text:
            nf.write(str(dict.get('filename') + '\n'))
            nf.write(str(dict.get('lenght')) + '\n')
            nf.write(str(dict.get('text') + '\n'))

write_new_file()
print('Файл создан')