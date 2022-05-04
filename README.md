# Tarea 1 Sistemas Distribuidos

## Integrantes

- Rodrigo Alvarez
- Valeria Fuentes

### Como ejecutar

Para ejecutar este proyecto de una manera "sencilla", necesitas instalar [Docker](https://docs.docker.com/get-docker/) y
[Docker Compose](https://docs.docker.com/compose/install/).

Basta con ejecutar:

```sh
docker-compose up
```

---

### Variables de entorno

En el repositorio existe un archivo `.env` de ejemplo, el cual tiene las configuraciones por default (user, passwod, host, database) que tendrá la base de datos de postgres levantada.

---

### API rest

Este proyecto levantará una API rest en el puerto `3000` el cual tiene una unica ruta **`/inventory/search`** la cual solo responde a request del tipo **GET**. A esta ruta se le puede pasar como query string el parametro `q` para obtener los resultados del inventario que tengan el string definido como valor de q.

**Ejemplo:**

```
http://localhost:3000/inventory/search [GET]
```

Tendrá una respuesta similar a:

```json
{
  "products_list": [
    {
      "id": 1,
      "name": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
      "price": 109.94999694824219,
      "category": "mens clothing",
      "count": 120
    },
    {
      "id": 2,
      "name": "Mens Casual Premium Slim Fit T-Shirts",
      "price": 22.299999237060547,
      "category": "mens clothing",
      "count": 259
    }
  ]
}
```

Y luego:

```
http://localhost:3000/inventory/search?q=Mens [GET]
```

Tendrá una respuesta similar a:

```json
{
  "products_list": [
    {
      "id": 2,
      "name": "Mens Casual Premium Slim Fit T-Shirts",
      "price": 22.299999237060547,
      "category": "mens clothing",
      "count": 259
    }
  ]
}
```

Filtrando de esta manera solo los productos que tengan dentro de **name** el string `"Mens".

---

### Configuración redis

Redis ha sido configurado montando el archivo redis.conf dentro del container en la ruta **`/opt/bitnami/redis/mounted-etc/overrides.conf`**, el cual define una memoria maxima de `885kb` y una politica de remoción de `LRU`. De la siguiente manera:

```
maxmemory 885kb
maxmemory-policy allkeys-lru
```
