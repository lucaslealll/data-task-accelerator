# Configuração do Ambiente de Desenvolvimento

## Pré-requisitos

- **Python 3.10** deve estar instalado no seu sistema.

## Passos para Configuração

1. **Crie um ambiente virtual local:**
      ```sh
      python3.10 -m venv .venv
      ```

2. **Ative o ambiente virtual:**

    Feche o terminal e abra novamente. Isso ajudará a garantir que o ambiente virtual seja ativado corretamente. Se você estiver usando o `VS Code`, ele pode perguntar se você deseja alterar o ambiente de execução para o recém-criado.

    *Se o ambiente não for ativado automaticamente, use o seguinte comando*:

    - Linux, macOS:
      ```sh
      source .venv/bin/activate
      ```
    - Windows:
      ```cmd
      .venv\Scripts\activate
      ```

3. **Instale as bibliotecas necessárias:**
    ```sh
    pip install -r requirements.txt
    ```

4. **O diretório está pronto para uso.**

---

### Notas Adicionais

- Para desativar o ambiente virtual, você pode usar o comando:
    ```sh
    deactivate
    ```
   - Toda vez que você abrir o projeto no VS Code, ele já sera identificado e inicializado automaticamente.
- Certifique-se de que todas as dependências estão listadas no arquivo `requirements.txt` para garantir que o ambiente seja configurado corretamente.
