import requests
import json
import html
from datetime import datetime
 
 
url = "https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId=7004&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1746399600&end=1747004400&_=1746736138904"
 
 
formador = "Rogélio Manuel Nascimento Palma Rodrigues"
 
try:
 
    resposta = requests.get(url)
    resposta.raise_for_status()
 
 
    eventos = resposta.json()
 
 
    for evento in eventos:
        descricao = html.unescape(evento.get("description", ""))
 
 
        if formador.lower() in descricao.lower():
            inicio_timestamp = evento['start']
            fim_timestamp = evento['end']
 
            inicio_data = datetime.fromtimestamp(inicio_timestamp)
            fim_data = datetime.fromtimestamp(fim_timestamp)
 
            print(f"Título: {evento['title']}")
            print(f"Início: {inicio_data.strftime('%d/%m/%Y %H:%M')}")
            print(f"Fim:    {fim_data.strftime('%d/%m/%Y %H:%M')}")
            print("-" * 40)
 
except requests.exceptions.RequestException as erro:
    print("Erro:", erro)
