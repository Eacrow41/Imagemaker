from fastapi import FastAPI
from src.generateplacas import placaspatentes

listaLetras = placaspatentes()

app = FastAPI(title='Python Imagemaker',
              description='Prueba tecnica Python Imagemaker',
              version='1.0.1')


#Ruta para la consulta de los IDs de los registros por el numero de la placa
@app.get("/placa/{num_placa}")
async def get_for_placa(num_placa):
    try:
        indice = listaLetras.index(num_placa)
        id_placa = format(indice)
        placa = int(id_placa)
        placa += 1
    except:
        placa = 'El numero de la placa no se encuentra en el listado.'

    return {"Id-Placa": placa}

#Ruta para la consulta de las placas de los registros por el numero del ID de la placa
@app.get("/id/{id_placa:int}")
async def get_for_id(id_placa):
    if (type (id_placa) == int) and (id_placa <= len(listaLetras)) and (id_placa > 0):
        id_placa -= 1
        placa = listaLetras[id_placa]

    else:
        placa = 'Valor de ID invalido, los valores permitidos son del N° 1 al ' + str(len(listaLetras))

    return {"N°-Placa": placa}


#Ruta para la consulta de las placas de los registros por el numero del ID de la placa, retorna el mensaje en caso de que el parametro sea STR
@app.get("/id/{id_placa}")
async def get_for_idstr(id_placa):
    placa = 'Valor de ID invalido, los valores permitidos son del N° 1 al ' + str(len(listaLetras))

    return {"N°-Placa": placa}