def divisores_exatos_e_primos():
    cont=0
    lista=[]

    try:
        num=int(input('digite um numero: '))
        if num<=0:
            print('digite um numero maior que zero')
        
        else:
            for i in range(num):
                i=i+1
                div=num%i
                if div==0:
                    cont=cont+1
                    lista.append(i)
        if len(lista)>1:
            print('o {} possui {} divisores exatos que são {}'.format(num,cont,lista))
        if len(lista)==2:
            print('o',num,'é primo')
        if len(lista)==1:
            print('o {} possui apenas um divisor exato que é ele mesmo'.format(num))
    except ValueError:
        print('digite apenas valores interiros')
    except ZeroDivisionError:
        print('não existe divisão por zero')
    except: 
        print('erro desconhecido')
while True:
    a=(input('para digitar um numero tecle enter ou P para encerrar: '))
    if a=='p' or a=='P':
        break
    else:
        divisores_exatos_e_primos()
