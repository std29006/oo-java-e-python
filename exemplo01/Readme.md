# Método main e argumentos de linha de comando

### Java

Em Java toda classe pública deverá ter obrigatoriamente o mesmo nome do arquivo `.java` onde a mesma é declarada. Só é permitido ter uma única classe pública por arquivo `.java`. Por fim, para que uma classe possa ser executada, é necessário que a mesma possua um método `public static void main(String[] args)`.

> `aluno:$ vi OlaMundo.java`

```java
public class OlaMundo {

    public static void helloWorld(){
        System.out.println("Hello World");
    }

    public static void main(String[] args) {
        if (args.length == 0){
            System.out.println("Olá mundo");
        }else{
            int contador = 0;
            for (String argumento : args) {
                System.out.println("argumento["+contador+"]: " + argumento);
                contador++;
            }
        }
        
        // invocando um método estático da classe
        helloWorld();
    }
}
```
#### Compilando e executando


```bash
javac OlaMundo.java
java OlaMundo Em Java
```

### Python3

Diferentemente de Java, em Python é possível criar *scripts* sem a obrigação de ter que criar uma classe.

Criando um *script* chamado `app-exemplo01.py`.

`vi app-exemplo01.py`

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def hello_world():
    print("Hello World")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Olá mundo")
    else:
        contador = 0
        for argumento in sys.argv:
            print("argumento[{}]: {}".format(contador, argumento))
            contador = contador + 1
    
    # invocando uma função do script atual        
    hello_world()
```

>    O uso do `if __name__ == '__main__':` é opcional, porém é interessante, caso queira garantir que as instruções só serão executadas se o *script* for interpretado e não quando for importado por algum outro *script*.



#### Executando


```shell
python3 app-exemplo01.py Em Python
```