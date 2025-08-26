

import json           
import os             

ARQUIVO = "tasks.json"  

def carregar_tarefas():
    """Carrega a lista de tarefas do arquivo JSON."""
    
    if not os.path.exists(ARQUIVO):  
        return []                   
    
    with open(ARQUIVO, "r", encoding="utf-8") as f: 
        try:
            dados = json.load(f)     
            
            return dados if isinstance(dados, list) else []
        except json.JSONDecodeError:
          
            return []

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
 
    with open(ARQUIVO, "w", encoding="utf-8") as f:   
        json.dump(tarefas, f, ensure_ascii=False, indent=2) 

def listar_tarefas(tarefas):
    """Exibe as tarefas numeradas."""
 
    if not tarefas:                                
        print("Nenhuma tarefa cadastrada.")    
        return  
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas, start=1):    
        status = "ok" if tarefa.get("done") else "nada"
        texto = tarefa.get("text", "")               
        print(f"{i:>2}. {status} {texto}")           

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa ao final da lista."""
    
    texto = input("Digite a nova tarefa: ").strip()  
    if not texto:                                     
        print("Tarefa vazia não foi adicionada.")
        return                                      
        
    nova = {"text": texto, "done": False}           
    tarefas.append(nova)                             
    salvar_tarefas(tarefas)                          
    print("Tarefa adicionada.")

def validar_indice(tarefas, entrada):
    """Converte a entrada para índice válido (base 1). Retorna índice 0-based ou None."""
   
    try:
        idx_humano = int(entrada)                  
    except ValueError:
        print("Índice inválido (use um número).")
        return None                                 
    
    if idx_humano < 1 or idx_humano > len(tarefas):  
        print("Índice fora do intervalo.")       
        return None                                  
    
    return idx_humano - 1                            

def alternar_conclusao(tarefas):
    """Marca ou desmarca uma tarefa como concluída."""
   
    listar_tarefas(tarefas)                         
    if not tarefas:                                
        return                                      
    
    escolha = input("Número da tarefa para alternar (feito/pendente): ").strip()
    idx = validar_indice(tarefas, escolha)           
    if idx is None:                                  
        return
   
    tarefas[idx]["done"] = not tarefas[idx].get("done", False)  
    salvar_tarefas(tarefas)                         
    novo_estado = "concluída" if tarefas[idx]["done"] else "pendente"
    print(f"Tarefa marcada como {novo_estado}.")

def remover_tarefa(tarefas):
    """Remove uma tarefa pelo número."""
    
    listar_tarefas(tarefas)                        
    if not tarefas:                             
        return                        
    # Pede o número a remover
    escolha = input("Número da tarefa para remover: ").strip()
    idx = validar_indice(tarefas, escolha)          
    if idx is None:                                  
        return
    
    texto = tarefas[idx].get("text", "")             
    conf = input(f"Confirmar remoção de: '{texto}'? (s/n): ").strip().lower()
    if conf != "s":                                 
        print("Remoção cancelada.")
        return
    
    tarefas.pop(idx)                               
    salvar_tarefas(tarefas)                          
    print("Tarefa removida.")

def menu():
    """Loop principal do programa (o balcão onde tudo acontece)."""
   
    tarefas = carregar_tarefas()                    
    
    while True:                                     
       
        print("\n==== GESTOR DE TAREFAS ====")      
        print("1) Adicionar tarefa")                 
        print("2) Listar tarefas")               
        print("3) Alternar concluída/pendente")     
        print("4) Remover tarefa")                
        print("0) Sair")                             
      
        opcao = input("Escolha: ").strip()           
        if opcao == "1":                             
            adicionar_tarefa(tarefas)               
        elif opcao == "2":                           
            listar_tarefas(tarefas)                  
        elif opcao == "3":                          
            alternar_conclusao(tarefas)             
        elif opcao == "4":                          
            remover_tarefa(tarefas)                 
        elif opcao == "0":                           
            print("Saindo. Até a próxima!")       
            break                                    
        else:
            
            print("Opção inválida. Tente novamente.")  

if __name__ == "__main__":   
    menu()                   
