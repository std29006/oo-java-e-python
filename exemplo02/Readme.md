# Declarando classes e modificadores de acesso

Crie uma classe para representar um Carro que deve ter um modelo e a velocidade atual. Um carro, por definição, não poderá ter velocidade negativa ou maior que 200 km/h. A classe Carro deverá implementar um método que permita imprimir facilmente os valores de seus atributos. Por fim, deverá ser possível alterar o modelo de uma instância já criada.

Ao instanciar um objeto Carro o usuário poderá fornecer um modelo; um modelo e uma velocidade; ou não fornecer nenhum dos dois. Nesse último caso, a instância deverá ter 'Fusca' em modelo e '0' para velocidade.



## Em Java

```java
public class Carro{
    private final int VELOCIDADE_MAXIMA = 200;

    private String modelo;
    private int velocidade;
    
    public Carro(){
        this.modelo = 'Fusca';
        this.velocidade = 0;
    }
    
    public Carro(String modelo){
        this.modelo = modelo;
        this.velocidade = 0;
    }
    
    public Carro(String modelo, int velocidade){
        this(modelo);
        this.setVelocidade(velocidade);
    }
    
    public void setVelocidade(int velocidade){
        if (velocidade > 0){
            if ((this.velocidade + velocidade) <= this.VELOCIDADE_MAXIMA){
                this.velocidade += velocidade;
            }else{
                this.velocidade = this.VELOCIDADE_MAXIMA;
            }
        }else{
            if ((this.velocidade + velocidade) >= 0){
                this.velocidade += velocidade;
            }else{
                this.velocidade = 0;
            }
        }
    }
    
    public String toString(){
        return "Modelo: " + this.modelo + ", velocidade: " + this.velocidade;
    }
}
```

### Instânciando objeto da classe Carro em Java

```java
Carro fusca = new Carro();
System.out.println(fusca);

Carro ferrari = new Carro('Ferrari testarossa', 100);
System.out.println(ferrari);
```


## Em Python

```python
class Carro:
    VELOCIDADE_MAXIMA = 200

    def __init__(self, modelo = 'Fusca', velocidade = 0):
        self.modelo = modelo
        self._velocidade = velocidade
        
    def alterar_velocidade(self, velocidade):
        if velocidade > 0:
            if (self._velocidade + velocidade) <= Carro.VELOCIDADE_MAXIMA:
                self._velocidade += velocidade
            else:
                self._velocidade = Carro.VELOCIDADE_MAXIMA
        else:
            if (self._velocidade + velocidade) >= 0:
                self._velocidade += velocidade
            else:
                self._velocidade = 0
                
    def __str__(self):
        return "Modelo: {}, velocidade: {}".format(self.modelo, self._velocidade)
```

### Instânciando objeto da classe Carro em Python

```python
fusca = Carro()
print(fusca)

ferrari = Carro('Ferrari testarossa', 100)
print(ferrari)
```

### Executando [exemplo](app-exemplo02.py) que está nesse diretório


```bash
python3 app-exemplo02.py
```