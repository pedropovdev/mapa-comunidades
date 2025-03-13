import folium
import pandas as pd
from branca.element import Html

# Carregar os dados
file_path = "Comunidades.xlsx"
df = pd.read_excel(file_path, sheet_name="comunidades_rotas")

# Criar um mapa centralizado na média das coordenadas
m = folium.Map(location=[df['y'].mean(), df['x'].mean()], zoom_start=5, width='100%', height='100%')

# Adicionar um título acima do mapa
titulo_html = '''
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; margin-top: 10px;">
        <h3 align="center" style="font-size:50px; margin-bottom: 10px;"><b>Roteiros Turísticos em Comunidades Quilombolas</b></h3>
        <div id="map" style="width: 60%; height: 60%;"></div>
    </div>
    '''
m.get_root().html.add_child(Html(titulo_html, script=True))

# Adicionar os pontos das comunidades ao mapa
for _, row in df.iterrows():
    folium.Marker(
        location=[row['y'], row['x']],
        popup=row['Comunidade'],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Salvar o mapa em um arquivo HTML
m.save("mapa_comunidades.html")

print("Mapa criado com sucesso! Abra 'mapa_comunidades.html' para visualizá-lo.")