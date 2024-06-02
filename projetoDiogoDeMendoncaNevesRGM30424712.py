import matplotlib.pyplot as plt; plt.rcdefaults() 
import numpy as np 
musicas = ('Lib Provisória', 'Sentadão', 'Combatchy', 'Surtada', 'Cheirosa') 
indice = np.arange(len(musicas)) 
acessos = [1068254,866216,849895,763652,758198] 
plt.bar(indice, acessos) 
plt.xticks(indice, musicas) 
plt.ylabel('Acessos') 
plt.title('Ranking do Spotify 31.dez.2019') 
plt.show()

###########################################

import matplotlib.pyplot as plt 
labels = 'Nenhum','Fundamental','Médio','Superior' 
sizes = [86026, 28525, 57394, 25286] 
colors = [ 'lightgray', 'orange', 'coral', 'red'] 
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90) 
plt.legend(patches, labels, loc="lower right") 
plt.axis('equal') 
plt.show()  

###########################################

import matplotlib.pyplot as plt  
fig, gnt = plt.subplots()  
gnt.set_ylim(0, 50)  
gnt.set_xlim(0, 160)  
gnt.set_xlabel('dias de projeto')  
gnt.set_ylabel('Tarefas')  
gnt.set_yticks([15, 25, 35])  
gnt.set_yticklabels(['Tarefa 1', 'Tarefa 2', 'Tarefa 3'])  
gnt.grid(True)  
gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (30, 9), facecolors =('tab:red'))  
gnt.broken_barh([(40, 50)], (20, 9), facecolors =('tab:green'))  
gnt.broken_barh([(110, 10), (150, 10)], (10, 9), facecolors ='tab:blue') 
