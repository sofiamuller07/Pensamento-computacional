Entradas:

três botões - escolhem o modo da máquina
um botão de desligar - desliga tudo
um potenciômetro - controla o brilho do LED
Saída:
Um LED RGB - muda de cor pra indicar o estado da máquina

componentes:

Botões: são a forma do operador dizer “quero esse modo”
Potenciômetro: funciona como um controle de intensidade, tipo um dimmer de luz
LED RGB: é o “visor” do sistema mostra em cores, o estado atual
Microcontrolador: é quem pensa tudo e toma decisões

regras de funcionamento:

só pode existir um modo ativo por vez
cada modo tem uma cor:
verde - tudo ok
amarelo - atenção
vermelho - situação crítica
se o eu apertar mais de um botão ao mesmo tempo, o sistema precisa decidir
o ideal é definir uma prioridade, por exemplo:  
vermelho ganha de todos
amarelo ganha do verde
o brilho do LED depende do potenciômetro
quanto mais alto o valor, mais forte a luz
se apertar o botão de desligar:
LED apaga
sistema zera

Explique como você utilizaria estruturas if para controlar o sistema


fila de comandos:
o código utiliza uma estrutura if / else if para garantir exclusividade.
a primeira condição verdadeira interrompe a verificação das demais. Se o botão de "desligar" ou "vermelho" for acionado, o sistema ignora os outros botões.
evita conflitos de cores e garante que o comando mais importante sempre domine.
controle de Intensidade 
Um potenciômetro atua como o regulador de energia do sistema.
o sinal analógico (0 a 1023) é convertido via software para uma escala de PWM (0 a 255).
esse valor final determina o quão forte a cor priorizada brilhará.
o LED operará em modo exclusivo ele exibirá apenas a cor de maior prioridade no momento, com o brilho ajustado em tempo real pelo operador através do potenciômetro.

