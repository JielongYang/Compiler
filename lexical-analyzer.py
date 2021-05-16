keywords = ['and','array','begin','bool','call','case','char','constant',
'dim','do','else','end','false','for','if','input','integer','not',
'of','or','output','procedure','program','read','real','repeat','set',
'stop','then','to','true','until','var','while','write']

signs = ['*','+','-',',',';','=','(',')','[',']']

code_list = ['null','and','array','begin','bool','call','case','char',
'constant','dim','do','else','end','false','for','if','input','integer','not',
'of','or','output','procedure','program','read','real','repeat','set',
'stop','then','to','true','until','var','while','write','ID','INT','CHAR',
'(',')','*','*/','+',',','-','.','..','/','/*',':',':=',';','<','<=','<>',
'=','>','>=','[',']']

src_code = ''
result_list = []

def read_file(filepath):
    src_code = ''
    for line in open(filepath,'r'):
        line = line.replace('\n', ' ')
        src_code += line
    return src_code


def is_letter(char):
    if char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z':
        return True
    else:
        return False
def is_digit(char):
    if char >= '0' and char <= '9':
        return True
    else:
        return False


def add_result(*args):
    code = str(code_list.index(str(args[0])))
    if len(args)>1:
        result_list.append('( '+code+', ' + str(args[1]) +' )')
    else:
        result_list.append('( '+code+', - )')
    return result_list

def src_code_to_result_list(src_code):
    i=0
    count=1
    while i < len(src_code):
        if src_code[i] == '/':
            if src_code[i+1] == '*':
                i+=2
                while src_code[i] != '*' or src_code[i+1] != '/':
                    i+=1
                    if i + 1 == len(src_code):
                        print('注释错误')
                        return
                i+=2
            else:
                add_result('/')
                i+=1
        elif src_code[i] == ':':
            if src_code[i+1] == '=':
                add_result(':=')
                i+=2
            else:
                add_result(':')
                i+=1
        elif src_code[i] == '.':
            if i+1< len(src_code) and src_code[i+1] == '.':
                add_result('..')
                i+=2
            else:
                add_result('.')
                i+=1
        elif src_code[i] == '<':
            if src_code[i+1] == '=':
                add_result('<=')
                i+=2
            elif src_code[i+1] == '>':
                add_result('<>')
                i+=2
            else:
                add_result('<')
                i+=1
        elif src_code[i] == '>':
            if src_code[i+1] == '=':
                add_result('>=')
                i+=2
            else:
                add_result('>')
                i+=1
        elif src_code[i] in signs:
            add_result(src_code[i])
            i+=1
        
        elif is_letter(src_code[i]):
            word =''
            while is_letter(src_code[i]) or is_digit(src_code[i]):
                word += src_code[i]
                i+=1
            if word in keywords:
                add_result(word)
            else:
                add_result('ID',count)
                count+=1
        elif is_digit(src_code[i]):
            digit = ''
            while is_digit(src_code[i]):
                digit += src_code[i]
                i+=1
            add_result('INT',count)
            count+=1
        elif src_code[i] == '\'':
            i+=1
            char = ''
            while src_code[i] != '\'':
                char += src_code[i]
                i+=1
                if i == len(src_code):
                    print('错误，单引号缺右引号')
                    return
            add_result('CHAR',count)
            count+=1
            i+=1
        else:
            i+=1

    return


def output():
    output = ''
    for i in range(0,len(result_list)):
        output += result_list[i] + '  '
        if (i+1)%5 == 0:
            output += '\n'
    print(output)
    return 

if __name__ == '__main__':
    src_code = read_file('test2.txt')
    src_code_to_result_list(src_code)
    output()