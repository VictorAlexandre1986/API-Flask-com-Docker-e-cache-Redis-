## Para rodar o app é preciso criar um ambiente virtual .

No Linux :
```
python3 -m venv venv
```
No Windows: 
```
python -m venv venv
```

## Depois é necessário acessar o ambiente virtual:

No Linux:
```
source venv/bin/activate
```

No Windows:
```
.\venv\Scripts\activate
```

## Depois instalar as dependencias:

```
pip install -r requirements.txt
```

## Para rodar o dockerfile :

```
docker-compose up --build
```
