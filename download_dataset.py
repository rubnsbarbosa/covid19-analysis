import csv
import json
import requests

def get_database_from_api():
    # API - aberta do IntegraSUS sobre os casos de coronavirus do Ceara
    url = 'https://indicadores.integrasus.saude.ce.gov.br/api/casos-coronavirus'
    req = requests.get(url)
    data = req.json()

    csv_file = open('dataset.csv','w')
    covid_writer = csv.writer(csv_file, delimiter=',')
    covid_writer.writerow(['Codigo Paciente','Estado Paciente','Codigo Municipio Paciente','Municipio Paciente','Bairro Paciente','Sexo Paciente','Idade Paciente','Data Notificacao','Data Inicio Sintomas'])

    for i in range(0, len(data)):
        dt = data[i]
        try:
            codigo_paciente = dt['codigoPaciente']
            estado_paciente = dt['estadoPaciente']
            codigo_municipio_paciente = dt['codigoMunicipioPaciente']
            municipio_paciente = dt['municipioPaciente']
            bairro_paciente = dt['bairroPaciente']
            sexo_paciente = dt['sexoPaciente']
            idade_paciente = dt['idadePaciente']
            data_notificacao = dt['dataNotificacao']
            data_sintomas = dt['dataInicioSintomas']
            covid_writer.writerow([codigo_paciente, estado_paciente, codigo_municipio_paciente, municipio_paciente, bairro_paciente, sexo_paciente, idade_paciente, data_notificacao, data_sintomas])

        except KeyError:
            if 'codigoPaciente' not in dt:
                covid_writer.writerow([None, estado_paciente, codigo_municipio_paciente, municipio_paciente, bairro_paciente, sexo_paciente, idade_paciente, data_notificacao, data_sintomas])
            elif 'estadoPaciente' not in dt:
                covid_writer.writerow([codigo_paciente, None, codigo_municipio_paciente, municipio_paciente, bairro_paciente, sexo_paciente, idade_paciente, data_notificacao, data_sintomas])
            elif 'codigoMunicipioPaciente' not in dt:
                covid_writer.writerow([codigo_paciente, estado_paciente, None, municipio_paciente, bairro_paciente, sexo_paciente, idade_paciente, data_notificacao, data_sintomas])
            elif 'municipioPaciente' not in dt:
                covid_writer.writerow([codigo_paciente, estado_paciente, codigo_municipio_paciente, None, bairro_paciente, sexo_paciente, idade_paciente, data_notificacao, data_sintomas])
            elif 'bairroPaciente' not in dt:
                covid_writer.writerow([codigo_paciente, estado_paciente, codigo_municipio_paciente, municipio_paciente, None, sexo_paciente, idade_paciente, data_notificacao, data_sintomas])
            elif 'sexoPaciente' not in dt:
                covid_writer.writerow([codigo_paciente, estado_paciente, codigo_municipio_paciente, municipio_paciente, bairro_paciente, None, idade_paciente, data_notificacao, data_sintomas])
            elif 'idadePaciente' not in dt:
                covid_writer.writerow([codigo_paciente, estado_paciente, codigo_municipio_paciente, municipio_paciente, bairro_paciente, sexo_paciente, None, data_notificacao, data_sintomas])
            elif 'dataNotificacao' not in dt:
                covid_writer.writerow([codigo_paciente, estado_paciente, codigo_municipio_paciente, municipio_paciente, bairro_paciente, sexo_paciente, idade_paciente, None, data_sintomas])
            elif 'dataInicioSintomas' not in dt:
                covid_writer.writerow([codigo_paciente, estado_paciente, codigo_municipio_paciente, municipio_paciente, bairro_paciente, sexo_paciente, idade_paciente, data_notificacao, None])

    csv_file.close()

if __name__ == "__main__":
    get_database_from_api()
