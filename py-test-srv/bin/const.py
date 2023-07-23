URL = 'https://py-srv:443'

GET_BY_FILTER_URL = URL + '/dog/3'

GET_ALL_URL = URL + '/dog'

STATIC = {
  "results": [
    {
      "breed": "Am Bulldog",
      "color": "White",
      "id": 1
    },
    {
      "breed": "Blue Tick",
      "color": "Grey",
      "id": 2
    },
    {
      "breed": "Labrador",
      "color": "Black",
      "id": 3
    },
    {
      "breed": "Gr Shepard",
      "color": "Brown",
      "id": 4
    }
  ]
}

DELETE_URL = URL + '/dog/1'

INSERT_URL = URL + '/dog/Poodle/Black'

SMOKE_URL = URL + '/'

SMOKE = {"hello": "world"}

UPDATE_URL = URL + '/dog/2/Mastif/White'
