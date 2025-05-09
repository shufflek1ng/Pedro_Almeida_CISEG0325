
import requests
from datetime import datetime


id = 9830
formador = "Rogélio Manuel Nascimento Palma Rodrigues"
list_ids = []  

try:
    while True:  
        
        response = requests.get(f"https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?"
                                f"command=_SelectAllSchedulesDataSetGivenByUserId&oId={id}&idField=DataValueField&titleField=DataTextField&"
                                f"startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&"
                                f"eventColorField=color&description=description&picField=pic&urlField=url&start=1746399600&end=1747004400")
        
        
        if "Sessão como Formador" in response.text and formador in response.text:
            print(f"\n\n--- Encontrado o formador: {formador}, ID: {id} ---")
            eventos = response.json()

            for evento in eventos:
                descricao = evento.get("description", "")

                if formador.lower() in descricao.lower():
                    
                    inicio_timestamp = evento['start']
                    fim_timestamp = evento['end']

                    inicio_data = datetime.fromtimestamp(inicio_timestamp)
                    fim_data = datetime.fromtimestamp(fim_timestamp)

                    
                    print(f"Título: {evento['title']}")
                    print(f"Início: {inicio_data.strftime('%d/%m/%Y %H:%M')}")
                    print(f"Fim:    {fim_data.strftime('%d/%m/%Y %H:%M')}")
                    print("-" * 40)

            list_ids.append(id)  
            break  
        else:
            print(f"ID {id} não tem eventos para o formador {formador}.")
        
        id += 1  

    print("\nIDs encontrados:", list_ids)

except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")