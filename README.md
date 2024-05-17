# P1-EC06-T08
Parte prática da prova 1 do módulo 6 de engenharia da computação.

## Estrutura de pastas

O projeto contém um workspace (diretório ```main_workspace```) com dois pacotes ROS2: ```ros_tutorials``` (para utilização do Turtlesim) e ```turtle_navigator``` (para execução do script que permite movimentar a tartaruga).

```
.
├── main_workspace
│   └──src
│       ├── ros_tutorials
│       └── turtle_navigator
├── .gitignore
├── README.md
└── requirements.txt
```

## Instalação

### Pré-requisitos

- Sistema operacional Linux (recomendado: Ubuntu 22.04.4 LTS)
- Git instalado e com chave SSH configurada
- ROS instalado

### Passo-a-passo

Para instalar e executar este projeto, siga os seguintes passos:

1. Clone este repositório abrindo uma janela de terminal no seu diretório de preferência e digitando o seguinte comando:

```git@github.com:RaiDeOliveira/P1-EC06-T08.git```

2. Certifique-se que todas as bibliotecas necessárias para executar o projeto estão instaladas através do comando:

```pip install -r requirements.txt```

3. Use o seguinte comando para que seja possível utilizar o ROS na janela de terminal atual:

```source /opt/ros/humble/setup.bash```

4. Digite os seguintes comandos para buildar o workspace:

```cd main_workspace```

```colcon build```

5. Digite o seguinte comando para poder utilizar os pacotes do workspace na janela de terminal atual:

```source install/local_setup.bash```

6. Digite o seguinte comando para iniciar o simulador Turtlesim:

```ros2 run turtlesim turtlesim_node```

7. Abra outra janela de terminal no mesmo diretório (```~/main_workspace/.```) e execute os seguintes comandos novamente para que o ROS e os pacotes do workspace funcionem na janela de terminal atual:

```source /opt/ros/humble/setup.bash```

```source install/local_setup.bash```

8. Digite o seguinte comando para movimentar a tartaruga:

```ros2 run turtle_navigator turtle_move```