# BOT PRA DIVULGAR NOS SERVERS ALHEIOS

### Como usar:
digite div em um chat qualquer em um servidor que o bot esteja, e ele irá divulgar dentro do servidor cujo id está presente na config. Para isso funcionar, o seu id deverá estar na lista de ids "adms" na config.

### Configuração:
```json
{
    "token":"token", // token do seu bot
    "server_id":123456789123456789, // id do servidor que você quer divulgar
    "adms":[123456789123456789, 123456789123456789] // ids dos usuários que poderão usar o comando "div"
}
```

### messages.txt:
Você pode colocar uma mensagem multilinha de sua preferência no messages.txt.
Para colocar várias, basta separá-las por "-=-=-end-=-=-"
Ex:
```
teste1
-=-=-end-=-=-
teste2
-=-=-end-=-=-
teste3
```

### blacklist.txt:
Aqui é a lista de ids de membros que não receberão as mensagens do seu bot.
Ex:
```
123456789123456789
123456789123456789
123456789123456789
123456789123456789
123456789123456789
123456789123456789
123456789123456789
123456789123456789
```