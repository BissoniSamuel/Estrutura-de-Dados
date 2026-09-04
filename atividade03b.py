from stack import Stack

if __name__ == "__main__":
    main_stack = Stack()
    min_stack = Stack()

    def push_aux(data):
        """
        Função para empilhar na pilha principal e atualizar a pilha de mínimos quando necessário.
        """
        #---- SEU CÓDIGO AQUI ----
        main_stack.push(data)
        if min_stack.is_empty() or data <= min_stack.peek():
            min_stack.push(data)

        #-------------------------

    def pop_aux():
        """
        Função para desempilhar da pilha principal e atualizar a pilha de mínimos quando necessário.
        """
        #---- SEU CÓDIGO AQUI ----
     
        if main_stack.is_empty():
            raise IndexError("Pilha principal vazia")

        data = main_stack.pop()

        if data == min_stack.peek():
            min_stack.pop()

        return data
        #-------------------------

    def get_min():
        """
        Função para retornar o mínimo atual.
        """
        #---- SEU CÓDIGO AQUI ----
        if min_stack.is_empty():
            raise IndexError("Nenhum elemento na pilha de mínimos")
        return min_stack.peek()


        #-------------------------

    # Testes
    print("\nEmpilhando: 5, 3, 7, 2, 8")
    push_aux(5)
    print(f"Min atual: {get_min()}")

    push_aux(3)
    print(f"Min atual: {get_min()}")

    push_aux(7)
    print(f"Min atual: {get_min()}")

    push_aux(2)
    print(f"Min atual: {get_min()}")

    push_aux(8)
    print(f"Min atual: {get_min()}")

    print("\nDesempilhando e mostrando o mínimo:")
    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    print(f"Min atual: {get_min()}")

    pop_aux()
    try:
        print(get_min())
    except IndexError as e:
        print(f"Erro esperado: {e}")