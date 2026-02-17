from datetime import datetime

class TASK:
    def __init__(self, nume):
        self.taskuri = {}  

        self.task_actual = None  
        self.timp_task_actual = None

        self.nume = nume 
        now = datetime.now()
        self.timp = now.strftime("%H:%M") 

    def timp_actual(self):
        print(self.timp)

    def adauga_task(self, x):
        lista_taskuri = x.split(' la ora ') 

        task, self.timp_task_actual = map(str.strip, lista_taskuri) 

        output_dictionar = {task: self.timp_task_actual} 
        self.taskuri.update(output_dictionar)

        print(f'Taskul {task}, ce trebuie indeplinit pana la ora {self.timp_task_actual}, a fost adaugat.\n')

    def calcul_timp(self, y):
        if y in self.taskuri: 

            timp_task_int = int(self.taskuri[y].replace(":", "")) 
            timp_actual_int = int(self.timp.replace(":", ""))

            d = (timp_task_int - timp_actual_int)  

            if d > 0: 
                print(f'Mai sunt {d // 100} ore ramase pentru taskul {y}')
                
            else:
                print("Termenul limita a fost depasit.")

        else:
            print(f'Taskul "{y}" nu a fost gasit.')

    def afiseaza_task(self):
        if self.taskuri:  
            print("Taskuri:")

            for task, timp_task_actual in self.taskuri.items(): 
                print(f"{task} la ora {timp_task_actual}.")

                self.calcul_timp(task) 

        else:
            print("Lista este goala, nu am ce sa afisez.")  

    def sterge_task(self):
        if self.taskuri:
            for task, timp_task_actual in self.taskuri.items(): 
                print(f" {task} la ora {timp_task_actual}.")

            task_de_sters = input("Alege taskul pe care doresti sa il stergi:\n")

            if task_de_sters in self.taskuri: 
                print(f'Taskul {task_de_sters}, ce trebuie indeplinit pana la ora {self.taskuri[task_de_sters]} a fost sters.')

                del self.taskuri[task_de_sters]

            else:
                print("Taskul respectiv nu este in lista, nu am ce sa sterg.")

        else: 
            print('Lista este goala, nu am ce sa sterg.')

    def edit_task(self):
        if self.taskuri:
            for task, timp_task_actual in self.taskuri.items():
                print(f" {task} la ora {timp_task_actual}.")

            task_de_editat = input("Alege taskul pe care doresti sa il editezi:\n")
            
            if task_de_editat in self.taskuri:
                nume_task_nou = input("Introduceti numele nou al taskului:\n")
                timp_task_nou = input("Introduceti noul timp al taskului (ex. format ora: 15:00):\n")

                print(f'Taskul {task_de_editat} a fost schimbat in {nume_task_nou}, de facut pana la ora {timp_task_nou}')

                self.taskuri[nume_task_nou] = timp_task_nou
                del self.taskuri[task_de_editat]

            else:
                print("Taskul cautat nu este in lista.")
        else:
            print('Lista este goala, nu am ce sa editez.')

    def completeaza_task(self):
        if self.taskuri:
            for task, timp_task_actual in self.taskuri.items(): 
                print(f" {task} la ora {timp_task_actual}.")

            task_completat = input("Alege taskul pe care l-ai completat:\n")

            if task_completat in self.taskuri: 
                print(f'Taskul {task_completat}, ce trebuie indeplinit pana la ora {self.taskuri[task_completat]} a fost completat.')

                del self.taskuri[task_completat]

            else:
                print("Taskul respectiv nu este in lista.")

        else: 
            print('Lista este goala.')

if __name__ == "__main__":

    nume_lista = input("Introduceti numele listei de taskuri:")

    lista_taskuri = TASK(nume_lista)
    lista_taskuri.timp_actual()

    while True:
        print("\nAlege o optiune pentru lista de taskuri",nume_lista, ":")
        print("1. Adauga un nou task")
        print("2. Afiseaza taskurile din lista")
        print("3. Sterge un task din lista")
        print("4. Editeaza un task din lista")
        print("5. Completeaza un task din lista")
        print("6. Exit")

        alegere = input("Introduceti numarul corespunzator optiunii pe care o doriti: ")

        if alegere == '1':
            n = input("Introduceti task (ex: x la ora 12:00): ")
            lista_taskuri.adauga_task(n)
        elif alegere == '2':
            lista_taskuri.afiseaza_task()
        elif alegere == '3':
            lista_taskuri.sterge_task()
        elif alegere == '4':
            lista_taskuri.edit_task()
        elif alegere == '5':
            lista_taskuri.completeaza_task()    
        elif alegere == '6':
            print("Program finalizat.")
            break
        else:
            print("Optiune invalida. Alege un numar intre 1 si 6.")

        go_back = input("Doresti sa te intorci in meniu? (da/nu): ")
        if go_back.lower() != 'da':
            print("Program finalizat.")
            break
