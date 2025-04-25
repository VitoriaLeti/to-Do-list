
from datetime import datetime

print("\nBem-vindo ao To-Do List!")
tarefas = [
    {"descricao": "Estudar Python", "prioridade": "alta", "data_limite": "hoje"},
    {"descricao": "Comprar leite", "prioridade": "baixa", "data_limite": "amanhã"},
    {"descricao": "Fazer exercícios", "prioridade": "média", "data_limite": "semana que vem"}
]

def mostrar_tarefas(tarefas):
    print("\nTarefas:")
    for tarefa in tarefas:
        print(f"Descrição: {tarefa['descricao']}, Prioridade: {tarefa['prioridade']}, Data Limite: {tarefa['data_limite']}")

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa"""
    descricao = input("Digite a descrição da tarefa: ")
    data_limite = input("Digite a data limite (opcional): ")
    if data_limite:
        data_limite = datetime.strptime(data_limite, "%d/%m/%Y")
    else:
        data_limite = None

    prioridade = input("Digite a prioridade (baixa, média, alta): ")
    while prioridade not in ["baixa", "média", "alta"]:
        prioridade = input("Prioridade inválida. Digite novamente (baixa, média, alta): ")

    tarefa = {
        "descricao": descricao,
        "data_limite": data_limite,
        "prioridade": prioridade,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def buscar_tarefa(tarefas):
    """Busca uma tarefa"""
    busca = input("Digite a palavra-chave para buscar: ")
    resultado = [tarefa for tarefa in tarefas if busca.lower() in tarefa['descricao'].lower()]
    if resultado:
        print("Resultados da busca:")
        for tarefa in resultado:
            print(f"{tarefa['descricao']} - {tarefa['prioridade']} - {tarefa['data_limite']}")
    else:
        print("Nenhum resultado encontrado.")
        mostrar_tarefas(tarefas)
        adicionar = input("Deseja adicionar uma nova tarefa com essa descrição? (s/n): ")
        if adicionar.lower() == 's':
            adicionar_tarefa(tarefas)
        else:
            print("Nenhuma tarefa adicionada.")


def marcar_tarefa_concluida(tarefas):
    """Marca uma tarefa como concluída"""
    nome_tarefa = input("Digite o nome da tarefa a ser marcada como concluída: ")
    for tarefa in tarefas:
        if tarefa['descricao'].lower() == nome_tarefa.lower():
            tarefa['concluida'] = True
            mostrar_tarefas(tarefas)
            print(f"Tarefa '{tarefa['descricao']}' marcada como concluída!")
            return
    print("Tarefa não encontrada!")



def remover_tarefa(tarefas):
    """Remove uma tarefa"""
    mostrar_tarefas(tarefas)
    nome_tarefa = input("Digite o nome da tarefa a ser removida: ")
    for tarefa in tarefas:
        if tarefa['descricao'].lower() == nome_tarefa.lower():
            tarefas.remove(tarefa)
            print(f"Tarefa '{tarefa['descricao']}' removida com sucesso!")

            return
    print("Tarefa não encontrada!")


def limpar_lista(tarefas):
    """Limpa a lista de tarefas"""
    tarefas.clear()
    print("Lista limpa com sucesso!")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Mostrar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Buscar Tarefa")
        print("4. Marcar Tarefa como Concluída")
        print("5. Remover Tarefa")
        print("6. Limpar Lista")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            mostrar_tarefas(tarefas)
        elif opcao == '2':
            adicionar_tarefa(tarefas)
        elif opcao == '3':
            buscar_tarefa(tarefas)
        elif opcao == '4':
            marcar_tarefa_concluida(tarefas)
        elif opcao == '5':
            remover_tarefa(tarefas)
        elif opcao == '6':
            limpar_lista(tarefas)
        elif opcao == '7':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

